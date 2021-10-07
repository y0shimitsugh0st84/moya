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

#display_aary=['1366x768','2560x1700','1366x768','2560x1600','2560x1440','1921x1080','2560x1440','1366x768','1440x900','1280x800','2560x1600','1440x900','1680x1050','2880x1800','1920x1200','1080x1920','768x1280','2160x4096','768x1366','1366x768','3840x2160','1600x900','1920x1080','2560x1440','1920x1200','2560x1440','2560x1600','1920x1080','1366x768','2560x1440','1366x768','3000x2000','2160x3840','768x1280','2304x1440','1366x768','1440x900','2560x1600','2880x1800','4096x2304','5120x2880','3840x2160','1920x1080','1280x800','1920x1080','1920x1080','1366x768','1920x1080','720x1280','480x800','1280x720','2560x1440','480x800','480x800','480x800','1080x1920','1080x1920','1080x1920','1080x1920','768x1280','1080x1920','1440x2560','1440x2560','1440x2560','768x1280','720x1280','1080x1920','480x854','540x960','540x960','540x960','1440x2560','1440x2560','1440x2560','720x1280','540x960','1080x1920','1080x1920','1080x1920','720x1280','800x1280','720x1280','480x800','480x800','480x800','720x1280','1080x1920','480x800','720x1280','720x1280','720x1280','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1080x1920','1280x720','1920x1080','1080x1920','1080x1920','720x1280','1080x1920','1080x1920','1080x1920','540x960','1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1280x720','1280x720','1280x720','1280x720','854x480','1920x1080','1920x1080','800x480','1920x1080','1920x1080','1920x1080','2560x1440','1920x1080','1920x1080','960x540','1920x1080','1920x1080','720x720','768x1280','960x540','1280x768','1440x1440','1280x720','1280x720','480x360','320x480','640x960','640x1136','750x1334','750x1334','1080x1920','750x1334','1080x1920','480x800','768x1280','480x800','480x800','480x800','480x800','768x1280','768x1280','1440x2560','1280x720','1440x2560','1440x2560','1080x1920','1080x1920','1440x2560','1600x1200','2048x1536','1280x800','768x1280','1280x800','1024x600','2048x1536','600x1024','800x1280','1200x1920','1280x720','800x1280','1200x1920','1200x1920','600x800','1024x600','1024x600','1280x800','1920x1080','1920x1080','800x1280','600x1024','800x1280','2048x1536','1280x800','800x1280','1280x800','1280x800','1024x600','1024x600','1280x800','1024x600','768x1024','1536x2048','768x1024','900x1600','1080x1920','1080x1920','1280x800','1280x800','1024x600','1280x800','1280x800','1280x800','1280x800','2048x1536','1920x1200','2560x1600','2560x1600','2048x1536','2048x1536','2732x2048','2048x1536','2048x1536','1280x800','2160x1440','2736x1824','2736x1824','2960x1440','2960x1440','750x1334','1080x1920','1125x2436','828x1792','1125x2436','1242x2688','640x1136','828x1792','1125x2436','1242x2688','1080x2400','1080x2310','1080x2400','1080x2340','1080x2340','1080x2340','1080x2340','1080x2400','1080x2400','1080x2400','1080x2340','1080x2340','1080x2340','1440x2560','1440x2560','1440x3200','1440x3088','1440x3200','1440x3040','1080x2400','1080x2280','1080x1920','1080x1920','2224x1668','2360x1640','750x1334','2160x1620','2388x1668','2732x2048','2048x1536','2224x1668','1170x2532','1080x2340','1170x2532','1284x2778']
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
	

