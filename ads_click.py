from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains # --------------> action muv the mouse
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,pyautogui,json,cnf

#os.environ['DISPLAY'] = ':0'


user_agent_list = cnf.user_agent_list
urls_GH=cnf.urls_GH


ads_links=['https://elated-nobel-943d26.netlify.app','https://flamboyant-kalam-54b358.netlify.app','https://serene-keller-a6f116.netlify.app']



firefox_options = Firefox_Options()
#firefox_options.binary = "/root/EXTRA/firefox-49.0b9/firefox/firefox";
#display = Display(visible=1, size=(860, 860))
#mouse=PyMouse()
#display.start

#firefox_options.add_argument("--headless")
###################################################################
def lets_go ():
	try:
		print("starting")
		my_vpn()
		display= Display(visible=1, size=(860, 860), use_xauth=False).start()

		change_time_zon()

		time.sleep(5)

		loop_all_ads_web()

		display.stop()

		init_fire()
	except Exception as errro:
		print(errro)
		display.stop()

#####################################################################
def change_time_zon():
	t_z=get_time_zon()
	print("Changing Time Zone ", end="")
	x = subprocess.Popen(['timedatectl', 'set-timezone', t_z])
	print('OK'+t_z)
	time.sleep(3)








###################################################################
def loop_all_ads_web():
	try:
		print("Loop")
		for ads_url in ads_links:
			print(ads_url)
			starter(ads_url)
			#t_z=get_time_zon()
			#print(t_z)
			#timedatectl set-timezone Africa/Algiers

			time.sleep(2)
		print("OK")





	except Exception as exception:
		print(str(exception))

###################################################################
def get_time_zon():
	response=requests.get('http://ipinfo.io')
	time_set=response.json()
	timezon=time_set['timezone']
	return timezon

####################################################################

def my_vpn ():
	init_fire()
	print("############################################################")
	print("KILLING OPENVPN ....",end=' ')
	random_vpn=random.choice(os.listdir(cnf.p_vpn_g))
	os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	time.sleep(3)
	print ("OK !!!!!")
	os.system("rm -rf /var/log/openvpn/openvpn.log")
	c_ip=iip()
	#print("Current IP :"+c_ip)
	print(random_vpn)
	path = cnf.p_vpn_g+random_vpn
	print("STARTING VPN !!!" , end="")
	x = subprocess.Popen(['openvpn', '--auth-nocache', '--config',path , '--log' , '/var/log/openvpn/openvpn.log'])
	time.sleep(10)
	with open ('/var/log/openvpn/openvpn.log', "r") as logfile:
				ac_ip=iip()
				if logfile.read().find('Sequence Completed') !=-1:
					print ("OK !!!!!")
					print("VPN STATUS = OK || "+ random_vpn +"||"+ ac_ip)
					#####--------------------------------------------###############################
					#starter()
					return [x ,True]
				else :
					print("VPN STATUS = OFF || "+ random_vpn )
					p_vpn_dead=cnf.p_vpn_dead

					processs="mv ..{} ..{}".format(random_vpn,p_vpn_dead)
					subprocess.run(processs ,shell=True)
					sys.exit(0)
					return [x ,False]

					try:
						x.kill()
						#my_vpn()
						#init_fire()
					except:
						pass
					
#############################################################################################









def build_driver():
	print("############################################################")
	print("srvice",end='')
	try:
		new_driver_path = cnf.new_driver_path
		new_binary_path = cnf.new_binary_path
		serv = Service(new_driver_path)
		user_agent = random.choice(user_agent_list)
		#print(user_agent)
		ops = Firefox_Options()
		ops.add_argument("--width=860")
		ops.add_argument("--height=860")
		fp=webdriver.FirefoxProfile()
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference('useAutomationExtension', False)
		fp.set_preference("general.useragent.override",user_agent)
		fp.set_preference("http.response.timeout",95)
		fp.set_preference('webdriver.load.strategy','unstable')
		fp.set_preference("modifyheaders.headers.count", 2)
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference("modifyheaders.headers.action0", "Add")
		fp.set_preference("modifyheaders.headers.name0", "x-msisdn")
		fp.set_preference("dom.push.enabled", False)
		fp.update_preferences()		
		ops.binary_location = new_binary_path
		ops.profile=fp
		driver = webdriver.Firefox(service=serv, options=ops)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		driver.set_page_load_timeout(79)
		print("   OK")
	except:
		print("   ERROR")

	return driver


def iip ():
	sourceee="http://ipecho.net/ip"
	r = requests.get(sourceee)
	ip=r.text
	return ip




def starter(url_ads):
	#init_fire()
	print("###########################Starting stage 01 #################################")
	#my_vpn ()
	url_booyah=url_ads
	print(url_booyah)
	print("Starting stage 01 : ",end='')
	#display.start()
	print("display OK")

	#time.sleep(5)
	try:
		print("MY BTTTC !!!!!!"+url_booyah)
		driver=build_driver()
		driver.get(url_booyah)
		time.sleep(5)
		maain_button=WebDriverWait(driver, 19).until(EC.presence_of_element_located((By.ID, 'rightbox')))
		time.sleep(12)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
		action = ActionChains(driver)
		action.move_to_element(maain_button).click().perform()
		#maain_button.send_keys(Keys.RETURN)
		#time.sleep(15)
		#maain_button.click()
		time.sleep(25)
		driver.quit()
	except Exception as error:
		print(error)


def init_fire():
	#os.system("clear")
	print("INIT TASKS ..... ", end='')
	try:
		#os.system("pkill firefox")#Xephyr geckodriver13
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#os.system("pkill Xephyr") Xvfb
		#os.system("pkill geckodriver13")
		os.system("rm -rf /tmp/*") 
		
		#display.start()
		#print("EEEEEEEEEEEEEEEEE!!!")
		time.sleep(5)
		#print("ENNNNNIIIIIIIIIITTTTT    !!!")
		#display.start()
		print(" OK !!!")
		print("############################################################")
	except:
		print(" NO  some_Error init_fire")


#hallo=cnf.p_vpn_g


#random_vpn=random.choice(os.listdir(cnf.p_vpn_g))
#print(hallo+user_agent_list[1])
#print (random_vpn)

#try:
#	my_vpn()
#except KeyboardInterrupt :
#	print("exit")
#	init_fire()
#	sys.exit(130)
#loop_all_ads_web()	
lets_go ()

