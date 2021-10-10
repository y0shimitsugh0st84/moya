import random,string , os ,time ,subprocess 
from datetime import *
from selenium import webdriver
from faker_e164.providers import E164Provider
from faker import Faker
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pyvirtualdisplay import Display
import requests
import io
from pydub import AudioSegment
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from stem import Signal
from stem.control import Controller
from activation_link import *
from activation_gmail_bitbucket import *
from mysql_python import *
from to_r import *
import curses
import speech_recognition as sr
#from fake_useragent import UserAgent
######################################################
#controller = Controller.from_port(port=9051)ay pydub
#apt-get install python-pyaudio python3-pyaudio ffmpeg
# pip3 install speechrecognition requests pyvirtualdisplay pydub
#apt-get install python-pyaudio python3-pyaudio ffmpeg 35.165.128.335.165.128.3
######################################################
import  j_conig
global arr_info
arr_info=[]
tagg=10
#######################################################""
########################################################################################################"
###################################### "               "################################################"
###################################### "   config      "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
########################################################################################################"
red=j_conig.EMAIL_CONFIG['sing_in_url']
domains_=j_conig.EMAIL_CONFIG['domain_']
github_username=j_conig.EMAIL_CONFIG['github_username']
github_proj=j_conig.EMAIL_CONFIG['github_project_name']
Profile_name=j_conig.EMAIL_CONFIG['Profile_name']
Binarry=j_conig.EMAIL_CONFIG['Binarry']
gecko_path=j_conig.EMAIL_CONFIG['gecko_path']
domains=[]
domains.append(domains_)
path_profile="/root/.mozilla/firefox/"+Profile_name

#hh=github_username.replace("liu","")
#hh=hh.replace("mac","")
display = Display(visible=1, size=(960, 860))
#display = Display(visible=1, size=(860, 600))
############################################################################################################
############################################################################################################

def vv(title):

	print(" # "+title+" ")
	print(" |")




reasonableCharacters = (string.digits + string.ascii_letters )
def password0(minimum=5, maximum=6):
    return ''.join(
        random.choice(reasonableCharacters) for x in range(
            random.randint(minimum, maximum)
        )
    )

def beep():
    print ("\a");print ("\a")
    print ("\a")

def generated():
	l0g("----------------------------------------> INFORMATIONS <-------------------------------------- ")
	print()
	print("GENERATING INFORMATION  : ",flush=True,end="")
	try:
		fake = Faker('en_US')
		fake.add_provider(E164Provider)
		nna=fake.name()
		first_name=fake.first_name()
		last_name=fake.last_name()
		phon_number =fake.e164(region_code="US", valid=True, possible=True)
		company_name=fake.bs() 
		#street_address=fake.street_address()
		address_=fake.address()
		tt=address_.split(",")
		street_address=tt[0].replace("\n"," ")
		street_address=street_address
		a_address_= address_.split()
		zip_code=a_address_[-1]
		city_0=tt[0].split("\n")
		city_1=city_0[1]
		city_=""
		add=city_1
		for i in add.split() :
			if i.isalpha() :
				city_+=i+" "

		street0_=city_0[0]
		dom=random.randint(1,len(domains))
		#timestamp = datetime.datetime.now()
		timestamp =time.strftime("%H%M%S", time.gmtime())
		vary=password0(4,4)
		t =  str(timestamp)+vary
		email_ja=nna.replace(" ",t)
		#balatch00@zoho.com
		#email_do="ezk0000za+"+email_ja+domains[dom-1]
		email_do=email_ja+domains[dom-1]

		email_do=email_do.lower()
		if ".@" in email_do:
			email_do=email_do.replace(".@","@")
		print ("DONNE")
		print("SESSION INFORMATIONS OF : ",flush=True,end="")
		print("[ "+email_do+" ]\n")
		return first_name,last_name,phon_number,company_name,email_do ,street_address,zip_code,city_,street0_
	except Exception as e:
		print(str(e))
		#input()
		generated()

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath('//*[@id="companyName"]')
    except :
        return False
    return True




def save_it(mail):
	with open('email__','a') as f:
	        f.write(mail+"\n")
	        f.close()
def save_it2(mail):
	with open('email__2','a') as f:
	        f.write(mail+"\n")
	        f.close()
	os.system("cat email__2  > /root/user_no_conf")
def save_it3(mail):
	with open('email__3','a') as f:
	        f.write(mail+"\n")
	        f.close()
	os.system("cat email__3  > /root/all_user_gitlab")
def save_it4(mail):
	with open('email__4','a') as f:
	        f.write(mail+"\n")
	        f.close()
	os.system("cat email__4  > /root/user_done")

########################################################################################################"
###################################### "               "################################################"
###################################### "     VPN       "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
########################################################################################################"

def get_myip():
	print("GET CURRENT IP SYSTEM : ",flush=True,end="")
	os.system("curl -s ipinfo.io/ip  > ipino")
	vpn_ip_get = open('ipino').read().splitlines()
	vpn_ip=vpn_ip_get[0]
	print(vpn_ip)
	
	return vpn_ip

def check_current_myip():
	#print("GET CURRENT IP SYSTEM : ",flush=True,end="")
	os.system("curl -s ipinfo.io/ip  > ipino")
	vpn_ip_get = open('ipino').read().splitlines()
	vpn_ip=vpn_ip_get[0]
	print(vpn_ip)
	
	return vpn_ip

def vpn_hidding():
	global real_ip
	global vpn_ip
	real_ip=""
	print(" # VPN HIDDING  ")
	print(" |")
	print(" |___|-----> ",flush=True,end="")
	try:
		real_ip=get_myip()
	except Exception as e:
		print("ERROR")
	#
	try:
		print(" |___|-----> STARTING VPN CONFIG : ",flush=True,end="")
		os.system("pkill openvpn && pkill xterm  && pkill firefox && pkill Xephyr")
		#lines = open('tccp').read().splitlines()
		##myline =random.choice(lines)
		#myline ="au293.nordvpn.com.tcp.ovpn"
		#config_vpn='openvpn /root/pn/ovpn_tcp/'+myline
		#config_vpn='openvpn /root/pn/ovpn_tcp/it39.nordvpn.com.tcp.ovpn'
		#os.system("xterm -e "+config_vpn+" &")############################################
		#############################################################################""
		#renew_tor()
		#l0g(myline)
		print(" |___|-----> CHECK CURRENT IP SYSTEM :",flush=True,end="")
		time.sleep(1)
		
		vpn_ip=check_current_myip()
		
	except Exception as e:
		print("ERROR")
	#
	try:
		print(" |___|-----> STATUS VPN : ",flush=True,end="")
		compar_ip_address(vpn_ip,real_ip)
	except Exception as e:
		print("ERROR")
	
def compar_ip_address(ip1,ip2):
	try:
		if real_ip in vpn_ip :
			
			l0g("VPN is down   [ "+real_ip+" ] <--*--> [ "+vpn_ip+" ]")
		else:
			l0g("VPN IS UP    [ "+real_ip+" ] <--=--> [ "+vpn_ip+" ]")
			#l0g("VPN UP  ---> "+vpn_ip+"<----- . . ."+real_ip)
	except:
		pass



########################################################################################################"
###################################### "               "################################################"
###################################### "   profile     "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
########################################################################################################"


def new_prof():
	print()
	l0g (" # new profile")
	print(" |")
	print(" |___|-----> ",flush=True,end="")
	try:
		print("STARTING DISPLAY  : " ,end="",flush=True)
		display.start()
		print( "OK" )
	except Exception as e:
		print("error")

	#input()
	print(" |___|-----> CREATING  PROFILE  : " ,end="",flush=True)
	remove_prof="rm -rf /root/.mozilla/firefox/"+Profile_name
	extract_prof="tar xf "+Profile_name+".tar.gz -C /root/.mozilla/firefox"
	empty_tmp="rm -rf /tmp/*"
	#print(" DONNE")
	
	#input()
	#vpn_ip=get_myip()
	try:
		subprocess.Popen(remove_prof, shell=True)
		time.sleep(1)
		subprocess.Popen(empty_tmp, shell=True)
	except:
		#by_by(driver)
		pass
	try:
		subprocess.Popen(extract_prof, shell=True)
		time.sleep(1)
		print("  O  K  ")
	except:
		by_by(driver)
		pass
def sstart():
	
	try:
		capabilities = webdriver.DesiredCapabilities().FIREFOX
		capabilities["marionette"] = True
		firefox_options = webdriver.FirefoxOptions()
		firefox_options.add_argument("--private")
		
		#firefoxOptions.AddArgument("--window-size").AddArgument("1920,1080")

		#profile = webdriver.FirefoxProfile(path_profile)
		profile = firefox_prof()
		binary = FirefoxBinary(Binarry)
		driver = webdriver.Firefox(firefox_options=firefox_options ,firefox_binary=binary , capabilities=capabilities , firefox_profile=profile , executable_path=gecko_path)
		driver.maximize_window()
	except Exception as r :
		print(str(r))
	return driver
	#TODO


def firefox_prof():

	#useragent = UserAgent()
	#print(useragent.random)
	profile = webdriver.FirefoxProfile(path_profile)
	#profile.set_preference("general.useragent.override", useragent.random)
	profile.set_preference('media.navigator.permission.disabled', True)
	profile.set_preference('browser.startup.homepage', 'about:blank')
	profile.set_preference("browser.privatebrowsing.autostart", True)
	profile.set_preference("browser.tabs.remote.autostart", False)
	profile.set_preference("browser.tabs.remote.autostart.1", False)
	profile.set_preference("browser.tabs.remote.autostart.2", False)
	profile.set_preference("dom.webnotifications.enabled", False)
	#profile.set_preference("network.cookie.cookieBehavior",2)
	#profile.set_preference('permissions.default.image', 2)
	profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',False)
	profile.set_preference("media.peerconnection.enabled", False)
	pss=1
	if pss==0:

		proxy ="127.0.0.1"
		port=9050
		profile.set_preference("network.proxy.type", 1)
		profile.set_preference("network.proxy.socks", proxy)
		profile.set_preference("network.proxy.socks_port", port)
		profile.set_preference("network.proxy.socks_version", 5)
		print("use proxy :",proxy,port)
		#proxy ="192.169.249.49"
		#port=2235
	profile.update_preferences()
	return profile

########################################################################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
########################################################################################################"
def c_url(driver):
	u_url=driver.current_url
	print(u_url)

	return 
########################################################################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
########################################################################################################"


def by_by(driver):
	driver.quit()
	os.system(" pkill Xephyr && pkill xterm && pkill openvpn && pkill xterm && pkill Xephyr")
	return
def b00t():
	os.system(" pkill Xephyr && pkill xterm && pkill openvpn && pkill xterm ")
	return
########################################################################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
###################################### "               "################################################"
########################################################################################################"
def go_820():
	l0g("----------------------------------------> START <-------------------------------------- ")
	#l0g("")
	commpany=arr_info[3]
	phoon=arr_info[2]
	okkk=arr_info[4].split("@")
	full_name=arr_info[0]+" "+arr_info[1]
	g_email="wa33iorx3+"+arr_info[4]
	docker_id=okkk[0]
	#docker_id=docker_id.replace("ezk0000za+","")
	passw=docker_id+"A*"
	if "." in docker_id :
		docker_id= docker_id.replace(".","")
	new_prof()
	driver=sstart()
	vpn_hidding()
	#
	#vpn_ip=get_myip()
	#	
	
	try:
		print(" |___|-----> BROWSER GO TO URL  : " ,end="",flush=True)
		print(red,end="",flush=True)
		#driver.get("https://browserleaks.com/ip")
		driver.get(red)
		print('   -------> OK')
	except:
		#input()
		print("erre")

	print("# REGISTRING  ")
	print(" |")
	print(" |___|-----> CHECK POINT 1  new_user_name : ",flush=True,end="")
	try:
		#driver.refresh()
		l0g(" [ ok ] ")
		eto_firstName=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.ID, 'new_user_name')))
		eto_firstName.click()
		
	except:
		driver.refresh()
		eto_firstName=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.primary-button.primary-button-blue')))
		print("create new account   go_820")
		by_by(driver)

	print(" |___|-----> FILLING INFORMATIONS : ",flush=True,end="")

	try:
		#c_url(driver)
		eto_firstName.click()
		user_name=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'new_user_name')))
		user_name.click()
		user_name.send_keys(full_name ,Keys.TAB, docker_id,Keys.TAB,g_email,Keys.TAB,g_email,Keys.TAB,passw,Keys.TAB,Keys.SPACE)
		l0g(" ok ")

	except Exception as e:
		print("error"+str(e))
		l0g("singup error  ")
		by_by(driver)
	try:
		print("error")
		
	except:
		print(" ")
		by_by(driver)
	try:
		#l0g("capatch")
		capatch(driver)
		if eta_capatcha == 0:
			by_by(driver)
			exit(0)
			return

	except:
		print("error capatch 000000")
		return
		by_by(driver)
	
	try:

		print("# SUBMIT  ")
		print(" |")
		driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
		time.sleep(1)
		donne_ok=WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.XPATH,'//span[@aria-checked="true"]')))
		driver.switch_to.default_content()
		time.sleep(1)
		submit_submit=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn-register.btn.qa-new-user-register-button')))
		submit_submit.click()
		time.sleep(1)
		submit_submit2=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-lg.btn-success')))
		print(" DONE !! ",flush=True,end="\n")
		os.system("  pkill xterm && pkill openvpn && pkill xterm")
		save_it2(docker_id)
		cmdo3="bash notconfirmed.sh "+docker_id
		#os.system(cmdo3)
		#by_by(driver)
		#return
	except:
		print("error")
		by_by(driver)
		return
	try:
		vv("email")
		#c_url(driver)
		submit_emailwaiting=WebDriverWait(driver, 13).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-lg.btn-success')))
		#l0g("wait email")
		os.system("  pkill xterm && pkill openvpn && pkill xterm")
	except:
		print("error email")
		l0g("erro wait email")
		by_by(driver)
	try:
		print("----------------- activation ----------------------------")
		os.system("pkill openvpn && pkill xterm")
		time.sleep(2)
		print("WAITING ACTIVATION LINK: "+"wa33iorx3+"+arr_info[4],flush=True,end="")
		time.sleep(20)
		activvat=gather_acces("wa33iorx3+"+arr_info[4])
		#u_url=driver.current_url
		driver.close()
		driver.get(activvat[0])
		print("ok")
	except:
		print("error activation ")
		by_by(driver)
	try:
		vv("login")
		driver.get("https://gitlab.com/users/sign_in")
		user_login=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'user_login')))
		user_login.send_keys(docker_id ,Keys.TAB, passw,Keys.TAB * 3 ,Keys.RETURN)
		#print("yepyepbaba123A* gitlb0"+docker_id+":"+passw)
		time.sleep(2)
		submit_emailwaiting=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.blank-state-body')))
		#time.sleep(5)
		driver.get("https://gitlab.com/projects/new")
		login_cred=docker_id+":"+passw
		save_it3(login_cred)
		doitt="echo "+login_cred+" > working0"
		os.system(doitt)
		trial_user_compan0=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'ci-cd-project-tab')))
		trial_user_compan0.click()

		time.sleep(3)
		
		try:
			u_url=driver.current_url
			#driver.get(u_url)
			#time.sleep(2)
			trial_user_compan0=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'ci-cd-project-tab')))
			trial_user_compan0.click()
			time.sleep(2)
			trial_user_compan0.send_keys(Keys.TAB *2,Keys.RETURN)
			#ting2=WebDriverWait(driver, 18).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.js-import-github')))
			time.sleep(2)
			ting=WebDriverWait(driver, 18).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-success'))).click()
		except Exception as e:
			print(str(e))
			by_by(driver)
			
		try:
		#btn js-import-github login_field btn btn-import btn-success js-import-all
			time.sleep(5)
			print("github :")
			c_url(driver)
			compan0=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'login_field')))
			time.sleep(1)
			compan0.send_keys(github_username,Keys.TAB ,"yepyepbaba123A*",Keys.RETURN)
			print("github ok")
		except Exception as e:
			print(str(e))
			by_by(driver)
		#js-oauth-authorize-btn
		try:
		#btn js-import-github login_field btn btn-import btn-success js-import-all
			time.sleep(2)
			print("oauth-authorize github :")
			#c_url(driver)
			compan0=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'js-oauth-authorize-btn')))
			time.sleep(1)
			compan0.click()
			print("github ok")
		except Exception as e:
			print("no oauth  ")
			pass
			

		print("ee st")
		time.sleep(7)
		try:
			print(u_url)
			ting=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-success.js-import-all')))
			ting.click()
			time.sleep(5)
			u_url=driver.current_url
			driver.get(u_url)
			print("ooooooooooooooooooooooo")
		except Exception as e:
			print(str(e))
			by_by(driver)
		print("ee okkkkk")
		try:
			print("set time")
			time.sleep(5)
			set_time="https://gitlab.com/"+docker_id+"/"+github_proj+"/settings/ci_cd"
			#input()
			driver.get(set_time)
			snoop=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.js-settings-toggle')))
			snoop.click()
			time.sleep(3)
			snoop.send_keys(Keys.TAB *3  ,Keys.DELETE,"4h",Keys.RETURN)
			compan0=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'project_build_timeout_human_readable')))
			compan0.click()
			compan0.send_keys(Keys.CONTROL + "a" ,Keys.DELETE,"4h",Keys.RETURN)
			print("ee okkkkk")
		except Exception as e:
			print(str(e))
			by_by(driver)

		try:
			print("GO TO SETTINGS: ",flush=True,end="")
			time.sleep(2)
			set_time="https://gitlab.com/"+docker_id+"/"+github_proj+"/settings/ci_cd"
			driver.get(set_time)
			snoop=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID,'js-pipeline-triggers')))
			snoop2=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.js-settings-toggle')))
			time.sleep(2)
			print("DONNE")
			print("GO TO PIPELINE : ",flush=True,end="")
			global iuy
			iuy=0
			list_items = driver.find_elements_by_tag_name("button")
			#print(str(list_items))
			#for bttt in list_items:
			#	if "btn js-settings-toggle" in bttt.get_attribute("class"):
			#		print(bttt.get_attribute("class"),str(iuy))
			#		time.sleep(2)
			#		bttt.click()
			#	iuy=iuy+1
			#input()
			list_items[30].click()
			print("DONNE")
			time.sleep(2)
			print("CREATING TOKENS : ",flush=True,end="")
			list_items[30].send_keys(Keys.TAB *2 ,docker_id,Keys.RETURN)
			time.sleep(5)
			ing=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-default.btn-sm')))
			print("DONNE")
			print("COPY TOKENS :  ",flush=True,end="")
			span_items = driver.find_elements_by_tag_name("td")
			time.sleep(5)
			for li in span_items:
				global kk
				kk=0
				anchor_tag = li.find_element_by_tag_name("span")
				kk=anchor_tag.text
				break
			print(kk)
			ing=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-default.btn-sm')))
			print("COPY PROJECT ID :  ",flush=True,end="")
			pre_items = driver.find_elements_by_tag_name("pre")
			project_id_in=pre_items[8].text
			project_id=project_id_in.replace(" https://gitlab.com/api/v4/projects/","")
			project_id=project_id.replace("/ref/REF_NAME/trigger/pipeline?token=TOKEN","")
			print(project_id)
			outtput=docker_id+"#"+project_id+"#"+kk
			save_it4(outtput)
			vello="curl -X POST -F token=z--z -F ref=master https://gitlab.com/api/v4/projects/x--x/trigger/pipeline"
			cmdo=vello.replace("z--z",kk)
			cmdo=cmdo.replace("x--x",project_id)
			for i in range(tagg):
				os.system(cmdo) #;os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo)
			#os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo);os.system(cmdo)
			cmdo2="bash gogo.sh "+outtput
			#os.system(cmdo2)
			insert_user(outtput)


			#input()
		except Exception as e:
			print(str(e))
			by_by(driver)

		#input()
		time.sleep(120)
		#display.stop()
		#driver.quit()
		by_by(driver)
		return
		

	except  Exception as e:
		print(" go_820 "+str(e))
		l0g("ACTIVATION error  ")
		display.stop()
		by_by(driver)



def capatch(driver):
	global eta_capatcha
	eta_capatcha=0
	print("\n # STARTING CAPATCHA  ")
	print(" |")
	try:
		while True :
			number_fra=len(driver.find_elements_by_tag_name("iframe"))
			#print(number_fra)find_elements_by_class_name
			if number_fra == 0 :
				time.sleep(3)
			else:
				driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
				recaptcha_ok=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,'//div[@class="recaptcha-checkbox-checkmark" and @role="presentation"]')))
				recaptcha_ok.click()
				time.sleep(1)
				#l0g("capatch 1  ! !")
				time.sleep(1)
				break
		driver.switch_to.default_content()
		time.sleep(3)
		driver.switch_to.default_content()
		time.sleep(3)
		number_fra=len(driver.find_elements_by_tag_name("iframe"))
		print("ok checkbox"+str(number_fra))
		time.sleep(1)
		#input()
		print(" |___|-----> CHECK POINT 2  SELECT AUDIO  : ",flush=True,end="")
		driver.switch_to.default_content()
		driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1])
		time.sleep(1)
		recaptcha_ok=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID,'recaptcha-audio-button'))).click()
		print("ok")
		time.sleep(2)
		print(" |___|-----> CHECK POINT 2  AUDIO RESOLVE : ",flush=True,end="")

		try:
			eto_firstName=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rc-audiochallenge-tdownload-link')))
			download_link = eto_firstName.get_attribute('href')
			request = requests.get(download_link)
			audio_file = io.BytesIO(request.content)
			converted_audio = io.BytesIO()
			audio_file = io.BytesIO(request.content)
			sound = AudioSegment.from_mp3(audio_file)
			dst = "test1.wav"
			sound.export(dst, format="wav")
			r = sr.Recognizer()
			with sr.WavFile("test1.wav") as source:
				audio = r.record(source)
			print(r.recognize_google(audio))
			#print("Transcription: " + r.recognize_google(audio))
			
		except:

			eto_firstName=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rc-doscaptcha-header-text')))
			print("NO "+eto_firstName.text)
			print(" |___|-----> EXIT : ",flush=True,end="")
			by_by(driver)
			os.system("pkill xterm  && pkill openvpn && pkill xterm && pkill Xephyr")
			exit(0)
		
		print(" |___|-----> CHECK POINT  SUBMIT THE RESULT : ",flush=True,end="")
		try:

			audio_output=r.recognize_google(audio)
			text_cap=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID,'audio-response')))
			text_cap.send_keys(audio_output)
			oooooo=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID,'recaptcha-verify-button'))).click()
			driver.switch_to.default_content()
			iframeso = driver.find_elements_by_tag_name("iframe")
			driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
			donne_ok=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,'//span[@aria-checked="true"]')))
			print("CAPTCHA KILLED  ")
		except:
			print("err")
		driver.switch_to.default_content()
		time.sleep(1)
		#os.system(" echo FILL INFORMATION  --  DONNE ! ! ")
		time.sleep(1)
		eta_capatcha=1
	except Exception as e:
		#print("error"+str(e))
		l0g("CAPTCHA error  ")
		by_by(driver)
		os.system("pkill Xephyr &&pkill openvpn && pkill xterm && pkill Xephyr")
		exit(0)


################################################
#################################################
#############################################
def capatch2(driver):
	try:
		#driver.refresh()
		
		#captchaFrame_name=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.col-sm-8.col-md-6.setup-form-container')))
		#captchaFrame_name.click()
		time.sleep(2)
		while True :
			number_fra=len(driver.find_elements_by_tag_name("iframe"))
			print(number_fra)
			if number_fra == 0 :
				time.sleep(5)
			else:
				number_fra=len(driver.find_elements_by_tag_name("iframe"))
				print(number_fra)
				driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
				time.sleep(2)
				recaptcha_ok=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,'//div[@class="recaptcha-checkbox-checkmark" and @role="presentation"]')))
				recaptcha_ok.click()
				time.sleep(5)
				driver.switch_to.default_content()
				l0g("capatch 1  ! !")
				time.sleep(5)
				break
		#for i in range(number_fra):
			#print(i)
			#try:
			#	driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[i])
			#	time.sleep(5)
			#	driver.find_element_by_xpath('//button[@id="recaptcha-audio-button"]').click()
			#	eto_firstName=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rc-audiochallenge-tdownload-link')))
			#	download_link = eto_firstName.get_attribute('href')
			#	print("ok"+download_link)
			#	driver.switch_to.default_content()
			#except:
			#	print("erroooooooooooo")
				#driver.switch_to.default_content()
		#number_fra2=len(driver.find_elements_by_tag_name("iframe"))
		#print(number_fra2)

		driver.switch_to.default_content()
		time.sleep(2)
		driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[-1])
		time.sleep(5)
		driver.find_element_by_xpath('//button[@id="recaptcha-audio-button"]').click()
		print("OK2&&&&&&&&&&&&&")
		#for i in range(number_fra):
			#try:
				#driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[i])
				#time.sleep(5)
				#driver.find_element_by_xpath('//button[@id="recaptcha-audio-button"]').click()
				#download_link = i.get_attribute('class')
				#print(download_link)
			#except:
				#print("nono")
				#driver.switch_to.default_content()
				#time.sleep(2)
		

		driver.switch_to.default_content()
		#time.sleep(2)
		#driver.switch_to.default_content()
		time.sleep(2)
		#print("number_fra")
		#print("ok checkbox")
		number_fra=len(driver.find_elements_by_tag_name("iframe"))
		print("ok checkbox"+str(number_fra))
		#driver.switch_to.default_content()
		time.sleep(3)

		try:
			driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[-1])
			time.sleep(5)
			#recaptcha_ok=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,'//button[@id="recaptcha-audio-button"]'))).click()
			print("ok audio switch_to")
			try:
				error_audio=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rc-doscaptcha-header-text')))
				print(error_audio.text)
			except:
				print("no error")
			
			time.sleep(1)
			eto_firstName=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rc-audiochallenge-tdownload-link')))
			download_link = eto_firstName.get_attribute('href')
			#print("ok"+download_link)
			request = requests.get(download_link)
			#print("ok3"+request.content)
			audio_file = io.BytesIO(request.content)
			converted_audio = io.BytesIO()
			audio_file = io.BytesIO(request.content)
			sound = AudioSegment.from_mp3(audio_file)
			#sound.export(converted_audio, format="wav")
			#converted_audio.seek(0)
			#recognizer = sr.Recognizer()
			#with sr.AudioFile(audio_source) as source:
				#audio = recognizer.record(source) # read the entire audio file
			#print(converted_audio)
			dst = "test1.wav"
			sound.export(dst, format="wav")
			r = sr.Recognizer()
			with sr.WavFile("test1.wav") as source:
				audio = r.record(source)
			print("Transcription: " + r.recognize_google(audio))
			audio_output=r.recognize_google(audio)
			text_cap=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID,'audio-response')))
			text_cap.send_keys(audio_output)
			oooooo=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID,'recaptcha-verify-button'))).click()
			
		except:
			pass#input()
		driver.switch_to.default_content()
		iframeso = driver.find_elements_by_tag_name("iframe")
		driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
		donne_ok=WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.XPATH,'//span[@aria-checked="true"]')))
		print("CAPTCHA KILLED  ")
		driver.switch_to.default_content()
		time.sleep(1)

		#input()
		os.system("FILL INFORMATION  --  DONNE ! ! ")
		time.sleep(2)
	except Exception as e:
		print("error"+str(e))
		#os.system("pkill openvpn && pkill xterm")
		l0g("CAPTCHA error  ")
##############################################################################################################


#################################################

def go_bitbucket():
	l0g("----------------------------------------> START <-------------------------------------- ")
	#l0g("")
	red="https://bitbucket.org/account/signup/"
	commpany=arr_info[3]
	phoon=arr_info[2]
	okkk=arr_info[4].split("@")
	full_name=arr_info[0]+" "+arr_info[1]
	g_email="b4bukbuk+"+arr_info[4]
	docker_id=okkk[0]
	#docker_id=docker_id.replace("ezk0000za+","")email_do="b4bukbuk+"
	passw=docker_id+"A*"
	if "." in docker_id :
		docker_id= docker_id.replace(".","")
	new_prof()
	driver=sstart()
	vpn_hidding()
	#
	#vpn_ip=get_myip()
	#	
	
	try:
		print(" |___|-----> BROWSER GO TO URL  : " ,end="",flush=True)
		print(red,end="",flush=True)
		#driver.get("https://browserleaks.com/ip")
		driver.get(red)
		print('   -------> OK')
	except:
		#input()
		print("erre")

	print("# REGISTRING  ")
	print(" |")
	print(" |___|-----> CHECK POINT 1  new_user_name : ",flush=True,end="")
########################################################################################################"
########################################################################################################"
########################################################################################################"
########################################################################################################"
	try:
		eto_firstName=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'js-email-proxy-field')))
		l0g("ready !!  ---> ")

		
	except:
		driver.refresh()
		eto_firstName=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.primary-button.primary-button-blue')))
		print("create new account   go_820")

	#time.sleep(2)
########################################################################################################"
########################################################################################################"
########################################################################################################"
	commpany=arr_info[3]
	phoon=arr_info[2]
	okkk=arr_info[4].split("@")
	full_name=arr_info[0]+" "+arr_info[1]
	g_email="b4bukbuk+"+arr_info[4]
	docker_id=okkk[0]
	docker_id=docker_id.replace("b4bukbuk+","")
	passw=docker_id+"A*"
	#passw="yepyepbaba123A*"gitlb0

	if "." in docker_id :
		docker_id= docker_id.replace(".","")
	print(arr_info)

	try:
		eto_firstName.click()
		user_name=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'js-email-proxy-field')))
		user_name.click()
		time.sleep(1)
		user_name.send_keys(g_email,Keys.RETURN)
		time.sleep(1)
		fulluser_name=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'js-full-name-field')))
		fulluser_name.click()

		fulluser_name.send_keys(full_name,Keys.TAB,passw)#,Keys.RETURN)	
		#js-full-name-field js-password-field js-continue-cta-link js-continue-cta-link

		#user_name.send_keys(full_name ,Keys.TAB, docker_id,Keys.TAB,g_email,Keys.TAB,g_email,Keys.TAB,passw,Keys.TAB,Keys.SPACE)
		#user_name.send_keys(Keys.TAB,arr_info[4],Keys.TAB,passw,Keys.TAB *2,Keys.RETURN)

		#user_name=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn-mktg.btn-primary-mktg.btn-large-mktg.f4.btn-block')))
		
		#time.sleep(10)
		#user_name.click()
		print("F I L L I N G    I N F O R M A T I O N S : ",flush=True,end="")
	except Exception as e:
		print("error"+str(e))
		#os.system("pkill openvpn && pkill xterm")
		l0g("singup error  ")
		#number_fra=len(driver.find_elements_by_tag_name("iframe"))
		#print(number_fra)
		#driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
		#fc_meta_audio_btn funcaptcha
			########################################################################################################"
	try:
		capatch2(driver)
	except:
		print("ola")
	driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
	time.sleep(1)
	donne_ok=WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.XPATH,'//span[@aria-checked="true"]')))
	print("CREATING ACCOUNT : ",flush=True,end="")
	l0g("CREATING ACCOUNT  ! !  ")
	driver.switch_to.default_content()
	time.sleep(3)
	try:
		sfulluser_name=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'js-continue-cta-link'))).click()
		#js-continue-cta-link js-continue-cta-link

	except:
		driver.quit()
	try:
		time.sleep(2)
		sfulluser_name=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'atlassian-id-email-verification')))
		#sfulluser_name.click()
		print("email now")
		os.system("pkill openvpn && pkill xterm")
		print("WAITING ACTIVATION LINK: ",flush=True,end="")
		l0g("WAITING ACTIVATION LINK ")
		print(g_email)
		time.sleep(12)
		activvat=gather_acces_bitbucket(g_email)
		print(activvat)
		driver.get(activvat[0])

		
		

		#os.system("aplay -q beep/l1.wav &>/dev/null")   js-username-field



		#input()
		submit_submit=WebDriverWait(driver, 150).until(EC.presence_of_element_located((By.ID,'js-username-field')))
		submit_submit.click()
		submit_submit.send_keys(docker_id,Keys.TAB,Keys.RETURN) 
		print(" DONE !! ",flush=True,end="\n")
		
		l0g( " submit DONE" )
		time.sleep(1)
		input()
		driver.get("https://g.codefresh.io/signup?ref=Sy304TkLN")
		input()
		try:
			submit_submit2=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-lg.btn-success')))
			#submit_submit2.click()
			print(" DONE !! ",flush=True,end="\n")
		except:
			pass
		#dcard styles__card___2O12Z styles__verify___1x7hx styles__card___gktOa

		try:
			submit_emailwaiting=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-lg.btn-success')))
			l0g("wait email")
			os.system("pkill openvpn")
			#os.system("echo 'wait email  ! ! ok' >> cchck ")
		except:
			l0g("erro wait email")
			exit(0)

			#input()


		
		#styles__title___2lbLz
		#confirm_email=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.styles__title___2lbLz')))
		#print(" email  DONE !! ",flush=True,end="\n")
		os.system("pkill openvpn && pkill xterm")
		print("WAITING ACTIVATION LINK: ",flush=True,end="")
		l0g("WAITING ACTIVATION LINK ")
		time.sleep(12)
		activvat=gather_acces(arr_info[4])
		print(activvat)
		driver.get(activvat[0])
		#https://customers.gitlab.com/trials/new?gl_com=true
		#https://gitlab.com/users/sign_in
		driver.get("https://gitlab.com/users/sign_in")
		#user_login user_password btn btn-success qa-sign-in-button
		user_login=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'user_login')))
		user_login.send_keys(docker_id ,Keys.TAB, passw,Keys.TAB * 3 ,Keys.RETURN)
		print("yepyepbaba123A* gitlb0"+docker_id+":"+passw)
		time.sleep(8)
		#blank-state-body
		submit_emailwaiting=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.blank-state-body')))
		#input()


		
		driver.get("https://g.codefresh.io/signup?ref=Sy304TkLN")
		trial_user_company_name=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'trial_user_company_name')))
		trial_user_company_name.send_keys(commpany,Keys.TAB,phoon,Keys.TAB,"1",Keys.TAB,Keys.ARROW_DOWN * 4,Keys.TAB ,Keys.RETURN)

		#nw_username input()
		try:
			#trial_user_namespace_id
			trial_user_company_name=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'trial_user_namespace_id')))
			print("0")
			trial_user_company_name.send_keys(Keys.ARROW_DOWN ,Keys.TAB ,Keys.RETURN)
		except:
			pass
		time.sleep(5)
		#d-none d-sm-block https://gitlab.com/import/github/new?ci_cd_only=true
		driver.get("https://gitlab.com/projects/new")
		login_cred=docker_id+":"+passw
		save_it3(login_cred)
		#cccmd="cd ~/dindin/ && echo "+login_cred+" >> okok && git add -u && git add -u && git add * && git commit -m 'v12' && git push --force"
		doitt="echo "+login_cred+" > working0"
		#os.system(cccmd) ci-cd-project-tab
		os.system(doitt)
		trial_user_compan0=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'ci-cd-project-tab')))
		trial_user_compan0.click()
		#trial_user_company_name trial_user_phone_number trial_user_number_of_users
		#os.system("pkill openvpn && pkill xterm  && pkill firefox")
		#btn btn-success
		#trial_user_compan0.send_keys(Keys.TAB *2,Keys.RETURN)
		time.sleep(4)
		try:
			trial_user_compan0.send_keys(Keys.TAB *2,Keys.RETURN)
			#ting2=WebDriverWait(driver, 18).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.js-import-github')))
			time.sleep(4)
			ting=WebDriverWait(driver, 18).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-success'))).click()
		except Exception as e:
			print(str(e))
			input()

		#btn js-import-github login_field btn btn-import btn-success js-import-all
		time.sleep(4)
		compan0=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'login_field')))
		compan0.send_keys("gitlb0",Keys.TAB ,"yepyepbaba123A*",Keys.RETURN)
		
		#time.sleep(4)
		ting=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-import.btn-success.js-import-all')))
		ting.click()
		try:
			ting.click()
		except:
			pass
		time.sleep(12)
		ting.send_keys(Keys.TAB *2,Keys.RETURN)
		time.sleep(8)
		#input()
		driver.get("https://gitlab.com/"+docker_id+"/git00/pipelines/new")
		#btn btn-success js-variables-save-button
		ting=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.btn.btn-success.js-variables-save-button'))).click()
		
		l0g("ID DOCKER activated  ")
		#input()
		os.system("pkill openvpn")
		time.sleep(5)
		#input()
		driver.quit()

	except  Exception as e:
		print(" go_820 "+str(e))
		#save_it(arr_info[4])
		#input()
		l0g("ACTIVATION error  ")
		#input()
		driver.quit()




os.system(" pkill modprob && pkill openvpn && pkill xterm  && pkill firefox && pkill Xephyr")
b00t()
try:
	arr_info=generated()
except:
	arr_info=generated()

#print(arr_info[4])
go_bitbucket()
#go_820()

#curl -X POST -H 'Content-type: application/json' --data  @<(cat <<EOF {"me": "$kk","something": $(date +%s)}EOF)  https://hooks.slack.com/services/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