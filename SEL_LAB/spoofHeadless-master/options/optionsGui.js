/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
(function(){
	"use strict";

	var scope;
	if ((typeof exports) !== "undefined"){
		scope = exports;
	}
	else {
		scope = {};
		window.scope.optionsGui = scope;
	}

	const logging = require("./logging");

	function createDescription(setting){
		var c = document.createElement("div");
		c.className = "content";

		var title = document.createElement("span");
		title.className = "title";
		title.textContent = browser.i18n.getMessage(setting.name + "_title");
		c.appendChild(title);

		var descriptionText = browser.i18n.getMessage(setting.name + "_description");
		if (descriptionText){
			var info = document.createElement("div");
			info.className = "info";
			c.appendChild(info);

			var description = document.createElement("div");
			description.className = "description";
			description.textContent = descriptionText;
			info.appendChild(description);
		}
		return c;
	}

	function createSelect(setting){
		var select = document.createElement("select");
		select.dataset.type = typeof setting.defaultValue;
		setting.options.forEach(function(value){
			var option = document.createElement("option");
			if (typeof value === typeof setting.defaultValue){
				option.value = value;
				if (setting.defaultValue === value){
					option.selected = true;
				}
				option.text = browser.i18n.getMessage(setting.name + "_options." + value) || value;
			}
			else {
				option.disabled = true;
				option.text = "\u2500".repeat(20);
			}
			select.appendChild(option);
		});
		return select;
	}
	
	var inputTypes = {
		number: {
			input: function(input, value){
				input.type = "number";
				input.value = value;
				return input;
			},
			updateCallback: function(input, value){
				input.value = value;
				return input.value;
			},
			getValue: function(input){
				return parseFloat(input.value);
			}
		},
		string: {
			input: function(input, value){
				input.type = "text";
				input.value = value;
				return input;
			},
			updateCallback: function(input, value){
				input.value = value;
				return input.value;
			},
			getValue: function(input){
				return input.value;
			}
		},
		boolean: {
			input: function(input, value){
				input.type = "checkbox";
				input.checked = value;
				input.style.display = "inline";
				return input;
			},
			updateCallback: function(input, value){
				input.checked = value;
				return input.checked;
			},
			getValue: function(input){
				return input.checked;
			}
		},
		object: false
	};

	function createInput(setting, url = ""){
		var type = inputTypes[typeof setting.defaultValue];
		var input;
		if (setting.options){
			input = createSelect(setting);
		}
		else {
			if (type){
				input = document.createElement("input");
				type.input(input, setting.defaultValue);
			}
		}
		if (type){
			setting.on(function(){type.updateCallback(input, setting.get(url));}, url);
			input.addEventListener("change", function(){
				var value = type.getValue(input);
				setting.set(value, url);
				logging.message("changed setting", setting.name, ":", value);
				
			});
		}
		if (setting.urlSpecific && url === ""){
			let container = document.createElement("div");
			container.className = "urlValues collapsed";
			container.appendChild(input);
			var collapser = document.createElement("span");
			collapser.classList.add("collapser");
			container.appendChild(collapser);
			collapser.addEventListener("click", function(){
				container.classList.toggle("collapsed");
				container.classList.toggle("expanded");
			});
			let urlTable = document.createElement("table");
			let caption = document.createElement("caption");
			caption.textContent = browser.i18n.getMessage(setting.urlContainer.name + "_title");
			urlTable.appendChild(caption);
			let body = document.createElement("tbody");
			urlTable.appendChild(body);
			let foot = document.createElement("tfoot");
			let footRow = document.createElement("tr");
			let footCell = document.createElement("td");
			footCell.colSpan = 3;
			let newInput = document.createElement("input");
			newInput.title = browser.i18n.getMessage("inputURL");
			footCell.appendChild(newInput);
			let footPlus = document.createElement("span");
			footPlus.classList.add("add");
			footPlus.textContent = "+";
			footPlus.addEventListener("click", function(){
				var url = newInput.value.trim();
				if (url){
					setting.set(setting.get(url), url);
					newInput.value = "";
				}
			});
			footCell.appendChild(footPlus);
			footRow.appendChild(footCell);
			foot.appendChild(footRow);
			urlTable.appendChild(foot);
			container.appendChild(urlTable);

			setting.urlContainer.on(function({newValue}){
				body.innerHTML = "";
				newValue.forEach(function(entry){
					let row = document.createElement("tr");
					let urlCell = document.createElement("td");
					urlCell.classList.add("url");
					urlCell.addEventListener("click", function(){
						var input = document.createElement("input");
						input.classList.add("urlInput");
						input.style.width = urlCell.clientWidth + "px";
						input.style.height = urlCell.clientHeight + "px";
						urlCell.innerHTML = "";
						urlCell.appendChild(input);
						input.title = browser.i18n.getMessage("inputURL");
						input.value = entry.url;
						input.focus();
						input.addEventListener("blur", function(){
							var url = input.value.trim();
							if (url){
								entry.url = url;
								setting.urlContainer.refresh();
							}
							urlCell.removeChild(input);
							urlCell.textContent = entry.url;
						});
					});
					urlCell.textContent = entry.url;
					row.appendChild(urlCell);
					let input = createInput(setting, entry.url);
					type.updateCallback(input, setting.get(entry.url));
					if (!entry.hasOwnProperty(setting.name)){
						input.classList.add("notSpecifiedForUrl");
					}
					let inputCell = document.createElement("td");
					inputCell.appendChild(input);
					row.appendChild(inputCell);
					let clearCell = document.createElement("td");
					clearCell.className = "reset";
					clearCell.textContent = "\xD7";
					clearCell.addEventListener("click", function(){
						setting.reset(entry.url);
					});
					row.appendChild(clearCell);
					body.appendChild(row);
				});
			});
			return container;
		}
		return input || document.createElement("span");
	}

	function createButton(setting){
		var button = document.createElement("button");
		button.textContent = browser.i18n.getMessage(setting.name + "_label");
		button.addEventListener("click", setting.action);
		return button;
	}

	function createInteraction(setting){
		var c = document.createElement("div");
		c.className = "content";

		var interaction;
		if (setting.action){
			interaction = createButton(setting);
		}
		else if (setting.inputs){
			interaction = document.createElement("span");
			setting.inputs.forEach(function(inputSetting){
				var input = createInput(inputSetting);
				input.classList.add("multiple" + setting.inputs.length);
				interaction.appendChild(input);
			});
		}
		else {
			interaction = createInput(setting);
		}

		interaction.classList.add("setting");
		interaction.dataset.storageName = setting.name;
		interaction.dataset.storageType = typeof setting.defaultValue;

		c.appendChild(interaction);
		return c;
	}

	function createSettingRow(setting){
		var tr = document.createElement("tr");
		tr.className = "settingRow";

		var left = document.createElement("td");
		left.appendChild(createDescription(setting));
		tr.appendChild(left);

		var right = document.createElement("td");
		right.appendChild(createInteraction(setting));
		tr.appendChild(right);

		return tr;
	}

	scope.createSettingRow = createSettingRow;
}());