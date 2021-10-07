import cnf
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service


from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests
from selenium.webdriver import ActionChains
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
print(profile_name)

#################################################################

display_aary=cnf.display_aary

random_display_chose=random.choice(display_aary)

display=random_display_chose.split(sep="x")
print(display[0]+"   "+display[1])

##################################################################


higo=int(display[0])
widee=int(display[1])
moz_wid="--width="+str(widee)
moz_hig="--height="+str(higo)

firefox_options = Firefox_Options()

########################################################################################################################################
def build_driver():
	print("############################################################")
	print("srvice",end='')
	try:
		new_driver_path = cnf.new_driver_path
		new_binary_path = cnf.new_binary_path
		serv = Service(new_driver_path)
		user_agent = random.choice(user_agent_list)
		ops = Firefox_Options()
		ops.add_argument(moz_wid)
		ops.add_argument(moz_hig)
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

########################################################################################################################################
def iip ():
	sourceee="http://ipecho.net/ip"
	r = requests.get(sourceee)
	ip=r.text
	return ip
########################################################################################################################################
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

########################################################################################################################################
def starter():
	#init_fire()
	print("###########################Starting stage 01 #################################")
	url_booyah=get_url()
	print(url_booyah)
	print("Starting stage 01 : ",end='')
	display = Display(visible=1, size=(widee,higo)).start()
	print("display OK")
	try:
		driver=build_driver()
		driver.maximize_window()#
		print(driver.execute_script("return navigator.userAgent;"))
		driver.get("https://wild-beauty.weebly.com/about.html")
		time.sleep(8)
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[1])
		time.sleep(1)
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[2])
		driver.get("https://wild-beauty.weebly.com/index.html")
		time.sleep(8)
		#display.start()
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[3])
		check_web(driver,url_booyah)
		driver.quit()
		print("Driver Stop !!!")
		os.system("pkill openvpn")
		print("vpn close")
		display.stop()
		print("Display Stop !!!")
	except Exception as a:
		print("something wrong   starter"+str(a))
		try:
			print("Display  ERRRRR Stop !!!")
		except:
			print("Display No Stop ERRRRRRRRRRRRRRR !!!")
			pass
		my_vpn ()
########################################################################################################################################
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
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
		time.sleep(3)
		print("OK !!")
		print("Click GO TO CAPTCHA  ..... : ",end='')
		main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.LINK_TEXT, 'here')))
		time.sleep(3)
		main_button.click()
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
			print("  SWITCH TO IFRAME "+ str(index) + " : ",end='')
			driver.switch_to.frame(index)
			print("  OK !!!!!!", end='')
			time.sleep(1)
			try:
				print("Button AUDIO CHECK CAPATCHA  ... : ",end='')#Get Link
				main_button=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.fbc-button-audio.fbc-button')))
				main_button.send_keys(Keys.RETURN)
				print("OK !!!!")#Get Link
				driver.switch_to.parent_frame()
				time.sleep(2)
				print("Back To Frames  !!!")#Get Link
				break
			except  Exception as b :
				print("NOT Found !!!")#Get Link
				driver.switch_to.parent_frame()
				pass
		driver.switch_to.parent_frame()
		time.sleep(4)

		print("SWETCH FRAM !!!",end='')#Get Link
		try:
			main_button=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-main')))
			time.sleep(2)
			main_button.click()
			time.sleep(4)
			print("  Submit OK !!!")#Get Link
		except  Exception as b :
			print(b)
			print("NOT Found SUBMI !!!")#Get Link
		time.sleep(2)
		main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		time.sleep(1)
		main_button.click()
		print("button  I'M HUMMEN BEEN !!!")#Get Link
		time.sleep(2)


		print("web page working GET THE LINK !!!")
		print("MY BTTTC !!!!!!", end='')
		driver.get("https://wild-beauty.weebly.com/index.html")
		time.sleep(3)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
		time.sleep(1)
		driver.execute_script("window.scrollTo(0, 0);window.scrollTo(0, 0);")
		ads_button=WebDriverWait(driver, 19).until(EC.presence_of_element_located((By.ID, '876903344444621682')))
		time.sleep(2)
		ads_button.send_keys(Keys.PAGE_DOWN)#rain_button.send_keys(Keys.PAGE_DOWN)
		time.sleep(2)
		ads_button.send_keys(Keys.PAGE_UP)
		time.sleep(10)
		action = ActionChains(driver)
		action.move_to_element(ads_button).click().perform()
		time.sleep(15)
		kads_button=WebDriverWait(driver, 19).until(EC.presence_of_element_located((By.ID, '876903344444621682')))
		print("OK !!!!!")


	except Exception as a:
		print("something wrong check web issu drive "+str(a))
		init_fire()
########################################################################################################################################
def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")
########################################################################################################################################
try:
	my_vpn()
except KeyboardInterrupt :
	print("exit")
	init_fire()
	sys.exit(130)
	

