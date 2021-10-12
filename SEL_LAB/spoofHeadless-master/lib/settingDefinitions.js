/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
(function(){
	"use strict";

	var settingDefinitions = [
		{
			name: "logLevel",
			defaultValue: 1,
			options: [0, 1, 25, 50, 75, 100]
		},
		{
			name: "urlSettings",
			defaultValue: [],
			urlContainer: true,
			entries: [
				{name: "url", defaultValue: ""}
			]
		},
		{
			name: "urls",
			defaultValue: [],
			dynamic: true,
			dependencies: ["urlSettings"],
			getter: function(settings){
				return settings.urlSettings.map(function(urlSetting){
					return urlSetting.url;
				});
			}
		},
		{
			name: "whiteList",
			defaultValue: ""
		},
		{
			name: "blackList",
			defaultValue: ""
		},
		{
			name: "blockMode",
			defaultValue: "fakeReadout",
			urlSpecific: true,
			options: [
				"blockReadout", "fakeReadout", "fakeInput", "askReadout", null,
				"blockEverything", "block", "ask", "allow", "allowEverything"
			]
		},
		{
			name: "minFakeSize",
			defaultValue: 1
		},
		{
			name: "maxFakeSize",
			defaultValue: 0
		},
		{
			name: "rng",
			defaultValue: "nonPersistent",
			options: ["white", "nonPersistent", "constant", "persistent"]
		},
		{
			name: "useCanvasCache",
			defaultValue: true
		},
		{
			name: "ignoreFrequentColors",
			defaultValue: 0
		},
		{
			name: "minColors",
			defaultValue: 0
		},
		{
			name: "fakeAlphaChannel",
			defaultValue: false
		},
		{
			name: "persistentRndStorage",
			defaultValue: ""
		},
		{
			name: "storePersistentRnd",
			defaultValue: false
		},
		{
			name: "persistentRndClearIntervalValue",
			defaultValue: 0
		},
		{
			name: "persistentRndClearIntervalUnit",
			defaultValue: "days",
			options: ["seconds", "minutes", "hours", "days", "weeks", "months", "years"]
		},
		{
			name: "lastPersistentRndClearing",
			defaultValue: 0
		},
		{
			name: "askOnlyOnce",
			defaultValue: "individual",
			options: ["no", "individual", "combined"]
		},
		{
			name: "askDenyMode",
			defaultValue: "block",
			options: ["block", "fake"]
		},
		{
			name: "showNotifications",
			defaultValue: true,
			urlSpecific: true
		},
		{
			name: "storeImageForInspection",
			defaultValue: false
		},
		{
			name: "notificationDisplayTime",
			defaultValue: 30
		},
		{
			name: "ignoreList",
			defaultValue: ""
		},
		{
			name: "showCallingFile",
			defaultValue: false
		},
		{
			name: "showCompleteCallingStack",
			defaultValue: false
		},
		{
			name: "enableStackList",
			defaultValue: false
		},
		{
			name: "stackList",
			defaultValue: ""
		},
		{
			name: "displayAdvancedSettings",
			defaultValue: false
		},
		{
			name: "displayDescriptions",
			defaultValue: false
		},
		{
			name: "isStillDefault",
			defaultValue: true
		},
		{
			name: "storageVersion",
			defaultValue: 0.3,
			fixed: true
		}
	];
	
	if ((typeof module) !== "undefined"){
		module.exports = settingDefinitions;
	}
	else {
		window.scope.settingDefinitions = settingDefinitions;
	}
}());