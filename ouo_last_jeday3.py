import cnf
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
import random,datetime,string , os ,time ,subprocess , sys , requests
import pyautogui


#os.environ['DISPLAY'] = ':0'

user_agent_list = cnf.user_agent_list
urls_GH=cnf.urls_GH


def get_url():
	url_booyah="https://ouo.io/"+random.choice(urls_GH)
	return url_booyah



def get_firefox_profile_dir():
    if sys.platform in ['linux', 'linux2']:
        import subprocess
        cmd = "ls -d /root/.mozilla/firefox/"
        p = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE)
        FF_PRF_DIR = p.communicate()[0][0:-2]
        FF_PRF_DIR_DEFAULT = str(FF_PRF_DIR,'utf-8')
    elif sys.platform == 'win32':
        import os
        import glob
        APPDATA = os.getenv('APPDATA')
        FF_PRF_DIR = "%s\\Mozilla\\Firefox\\Profiles\\" % APPDATA
        PATTERN = FF_PRF_DIR + "*default*"
        FF_PRF_DIR_DEFAULT = glob.glob(PATTERN)[0]
 
    return FF_PRF_DIR_DEFAULT

profile_name=get_firefox_profile_dir()





firefox_options = Firefox_Options()
#firefox_options.binary = "/root/EXTRA/firefox-49.0b9/firefox/firefox";
display = Display(visible=1, size=(860, 860))
#mouse=PyMouse()
#display.start

#firefox_options.add_argument("--headless")




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
		#		driver = webdriver.Firefox(firefox_profile=fp , service=serv, options=ops)
		#driver.maximize_window()
		driver.set_page_load_timeout(79)
		#driver.set_window_size(500,500)
		print(str(driver.get_window_size())+" Ok  !!!")
		#driver.implicitly_wait(30)
		print("   OK")
	except:
		print("   ERROR")

	return driver


def iip ():
	sourceee="http://ipecho.net/ip"
	r = requests.get(sourceee)
	ip=r.text
	return ip

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
	time.sleep(20)
	with open ('/var/log/openvpn/openvpn.log', "r") as logfile:
				ac_ip=iip()
				if logfile.read().find('Sequence Completed') !=-1:
					print ("OK !!!!!")
					print("VPN STATUS = OK || "+ random_vpn +"||"+ ac_ip)
					#####--------------------------------------------###############################
					starter()
					return [x ,True]
				else :
					print("VPN STATUS = OFF || "+ random_vpn )
					p_vpn_dead=cnf.p_vpn_dead
					processs="mv ..{} ..{}".format(random_vpn,p_vpn_dead)
					subprocess.run(processs ,shell=True)
					return [x ,False]

					try:
						x.kill()
						my_vpn()
						#init_fire()
					except:
						pass






def starter():
	#init_fire()
	print("###########################Starting stage 01 #################################")
	#my_vpn ()
	url_booyah=get_url()
	print(url_booyah)
	print("Starting stage 01 : ",end='')
	display.start()
	print("display OK")

	#time.sleep(5)

	try:
		driver=build_driver()
		print(driver.execute_script("return navigator.userAgent;"))
		time.sleep(5)
		driver.get("https://serene-keller-a6f116.netlify.app/index.html")
		
		driver.execute_script("window.open('');")
		
		driver.switch_to.window(driver.window_handles[1])
		
		driver.get("https://elated-nobel-943d26.netlify.app/index.html")
		time.sleep(15)
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[2])

		driver.maximize_window()# display.start()
		#driver.execute_script("window.open('');")
		#driver.switch_to.window(driver.window_handles[3])
		check_web(driver,url_booyah)
		driver.quit()
		print("Driver Stop !!!")
		os.system("pkill openvpn")
		print("vpn close")
		#
		#
		#
		display.stop()
		print("Display Stop !!!")
		#my_vpn()
	except Exception as a:
		print("something wrong   starter"+str(a))
		try:
			print("Display  ERRRRR Stop !!!")
			#driver.quit()
			#display.stop()
		except:
			print("Display No Stop ERRRRRRRRRRRRRRR !!!")
			pass
		#init_fire()
		#driver.quit()
		my_vpn ()

def check_web(driver , uur):
	print("###########################CHECK WEB DRIVER  CHECK#################################")
	print("CHECK WEB DRIVER  CHECK .....")
	driver.maximize_window()
	try:
		print("OPEN URL  CHECK .....",end='')
		#input('test')
		#driver.get("http://httpbin.org/headers")
		#input("iiii")
		driver.get(uur)
		time.sleep(2)
		#input('rrrr')
		pyautogui.dragTo(100,120)
		#input('rrrr')
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
		#driver.set_page_load_timeout(2)
		time.sleep(3)
		print("OK !!")
		###########################################################################################
		#input('Press Enter To CHECK CAPATCHA')
		# Your sweet business logic applied to iframe goes here.
		#element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.class, "ng-binding ng-scope")))
		print("Click GO TO CAPTCHA  ..... : ",end='')
		main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.LINK_TEXT, 'here')))
		#driver.refrech()
		#driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.5);window.scrollTo(0, document.body.scrollHeight/1.7);")
		time.sleep(3)
		source =WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.LINK_TEXT, 'here')))
		action = ActionChains(driver)
		action.move_to_element(source).click().perform()
		#input("hihi")
		#
		#
		#
		#main_button.click()
		#
		#
		#
		#
		print("  OK !!!!!!")
		time.sleep(3)
		rain_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.container')))
		time.sleep(3)

		rain_button.send_keys(Keys.PAGE_DOWN)
		time.sleep(3)

		main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-main')))

		iframes = driver.find_elements_by_xpath("//iframe")
		print(len(iframes))
		for index, iframe in enumerate(iframes):
			#print(index)
			#print(iframes[index])
			print("  SWITCH TO IFRAME "+ str(index) + " : ",end='')
			driver.switch_to.frame(index)
			print("  OK !!!!!!", end='')
			time.sleep(1)
			try:
				#input('botton clicked')
				print("Button AUDIO CHECK CAPATCHA  ... : ",end='')#Get Link
				main_button=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.fbc-button-audio.fbc-button')))
				#print("OK !!!!")#Get Link
				#time.sleep(4)
				#main_button.click()
				#time.sleep(2)
				#input('botton clicked 0000000000')
				main_button.send_keys(Keys.RETURN)
				print("OK !!!!")#Get Link
				#print("button 010101010101010 CHECK CAPATCHA  !!!")#Get Link
				#time.sleep(2)
				driver.switch_to.parent_frame()
				time.sleep(2)
				print("Back To Frames  !!!")#Get Link
				break
			except  Exception as b :
				#print(b)
				print("NOT Found !!!")#Get Link
				driver.switch_to.parent_frame()
				#time.sleep(4)
				pass
		#input('botton clicked 0000000000')
		driver.switch_to.parent_frame()
		time.sleep(4)

		print("SWETCH FRAM !!!",end='')#Get Link
		try:
			main_button=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-main')))
			time.sleep(2)
			#print("Found submit !!!")#Get Link
			main_button.click()
			time.sleep(4)
			print("  Submit OK !!!")#Get Link
			#main_button.send_keys(Keys.RETURN)
		except  Exception as b :
			print(b)
			print("NOT Found SUBMI !!!")#Get Link
		time.sleep(2)
		#print(iframes.get_attribute('href'))
		#input('Press Enter -- index-- To Continue')
        # Your sweet business logic applied to iframe goes here.

		main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		#driver.refrech()
		time.sleep(1)
		main_button.click()
		print("button  I'M HUMMEN BEEN !!!")#Get Link
		#driver.refrech()
		time.sleep(2)
		#second_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		#time.sleep(5)
		#second_button.click()
		#print("second_button cliked !!!")
		#time.sleep(3)
		#input('waitiiiiii')



		print("web page working GET THE LINK !!!")
		

		#time.sleep(5)
		
		#try:
		#	main_button=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		#except:
		#	driver.get("https://cocky-bose-de943a.netlify.app/index.html")
		#	print("EEEEEEEEEEEEEEEEE!!!")
		#	time.sleep(1)
		#	pass


		print("MY BTTTC !!!!!!", end='')
		driver.get("https://serene-keller-a6f116.netlify.app/index.html")
		time.sleep(3)
		maain_button=WebDriverWait(driver, 19).until(EC.presence_of_element_located((By.ID, 'rightbox')))
		time.sleep(3)
		#maain_button.send_keys(Keys.RETURN)
		time.sleep(5)
		maain_button.click()
		time.sleep(10)
		print("OK !!!!!")
		#https://app.netlify.com/sites/flamboyant-kalam-54b358
		print("MY BTTTC !!!!!!", end='')
		driver.get("https://flamboyant-kalam-54b358.netlify.app/index.html")
		time.sleep(3)
		maain_button=WebDriverWait(driver, 19).until(EC.presence_of_element_located((By.ID, 'rightbox')))
		time.sleep(3)
		#maain_button.send_keys(Keys.RETURN)
		time.sleep(5)
		maain_button.click()
		time.sleep(10)
		print("OK !!!!!")


	except Exception as a:
		print("something wrong check web issu drive "+str(a))
		##try:
			##driver.quit()
			#display.stop()
		##except:
			##pass
		##driver.close()
		init_fire()
		#input('endddddddddddddd')
		#my_vpn ()

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
try:
	my_vpn()
except KeyboardInterrupt :
	print("exit")
	init_fire()
	sys.exit(130)
	

