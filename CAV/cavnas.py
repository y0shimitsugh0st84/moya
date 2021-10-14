import cnf_bvb
import emoji
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,re
from selenium.webdriver import ActionChains
#import pyautogui
import json

#ENV['TZ'] = 'Africa/Algiers'

urls_BVB=cnf_bvb.random_url
#####################################
random_display_chose=cnf_bvb.random_display_chose
width=cnf_bvb.width
height=cnf_bvb.height

moz_wid="--width="+str(width)
moz_hig="--height="+str(height)

######################USER AGENT ###################################################
user_agent = cnf_bvb.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]

######################################################################################################
def iip ():
	#sourceee="ipecho.net"
	os.system("curl -s ipinfo.io > ipifo.json")
	f = open ('ipifo.json', "r")
	data = json.loads(f.read())
	#r = requests.get(sourceee)
	ip=data['ip']
	tz=data['timezone']
	loc=data['loc']
	country=data['country']
	print(ip + " "+tz+" "+loc)
	return ip,tz
########################################################################################################################################
def my_vpn ():
	init_fire()
	print("############################################################")
	print("KILLING OPENVPN ....",end=' ')
	random_vpn=random.choice(os.listdir(cnf_bvb.p_vpn_g))
	os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	time.sleep(3)
	print ("OK !!!!!")
	os.system("rm -rf /var/log/openvpn/openvpn.log")
	c_ip,tz=iip()
	print(random_vpn)
	path = cnf_bvb.p_vpn_g+random_vpn
	print("STARTING VPN !!!" , end="")
	x = subprocess.Popen(['openvpn', '--auth-nocache', '--config',path , '--log' , '/var/log/openvpn/openvpn.log'])
	time.sleep(12)
	with open ('/var/log/openvpn/openvpn.log', "r") as logfile:
				
				if logfile.read().find('Sequence Completed') !=-1:
					print ("OK !!!!!")
					ac_ip,tz=iip()
					os.environ['TZ'] = tz
					print("VPN STATUS = OK || "+ random_vpn +"||"+ ac_ip+"||"+ tz)
					#####--------------------------------------------###############################
					#starter()
					return [x ,True]
				else :
					print("VPN STATUS = OFF || "+ random_vpn )
					p_vpn_dead=cnf_bvb.p_vpn_dead
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


########################################################################################################################################
def build_driver():
	print("BUILDING PROFILE DRIVER  ...... ",end='')
	try:
		new_driver_path = cnf_bvb.new_driver_path
		new_binary_path = cnf_bvb.new_binary_path
		serv = Service(new_driver_path)
		fp = webdriver.FirefoxProfile()
		#user_agent = cnf_bvb.user_agent

		#firefox_options = Firefox_Options()

		ops = Firefox_Options()
		#ops.add_argument("--private")
		ops.add_argument(moz_wid)
		ops.add_argument(moz_hig)
		
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference('useAutomationExtension', False)
		#fp.set_preference("http.response.timeout",95)privacy.resistFingerprinting
		fp.set_preference("general.useragent.override",user_agent)
		fp.set_preference('webdriver.load.strategy','unstable')
		fp.set_preference("modifyheaders.headers.count", 2)
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference("modifyheaders.headers.action0", "Add")
		fp.set_preference("modifyheaders.headers.name0", "x-msisdn")
		fp.set_preference("dom.push.enabled", False)
		fp.set_preference("media.peerconnection.enabled", False)
		fp.set_preference("privacy.resistFingerprinting", True)
		fp.set_preference("general.useragent.locale","fr")
		#fp.set_preference("webgl.disabled", True)
		#webgl.disabled




		fp.update_preferences()
		ops.binary_location = new_binary_path
		ops.profile=fp
		#driver = webdriver.Firefox(service=serv, options=ops)
		#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		#driver.set_page_load_timeout(79)

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except Exception as error:
		print("    Error !!!!! ----->"+str(error))
	return serv ,ops

##################################################################################################
########################################################################################################################################
def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")
########################################################################################################################################


####################################################################################################

#####################################################################################################

def stage_1():
	try:
		#print (urls_BVB)
		os.system("rm -rf /tmp/*") 
		os.system("clear && sleep 5") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+urls_BVB+' :check_mark_button: :alien:'))
		print(emoji.emojize("Resolution : "+random_display_chose+' :check_mark_button: :alien:'))
		#####TO DO PRINT ONLY THE SYSTEM
		#print(width+"x"+height)
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")

	except Exception as error:
		print (str(error))
#####################################################################################################
def product_page(driver):  ##coords and dimensions to scroll through page
    container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kcarterlink')))
    #container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'here')))
    #driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center'});", container) ##scroll to product
    #kcarterlink
    action = webdriver.ActionChains(driver)
    action.move_to_element(container)
    action.perform()
    containerLoc = container.location
    containerSize = container.size
    startY = containerLoc["y"]
    height0 = containerSize["height"]
    container.click()
    container_timezon = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, '//*[@id="results"]/div[3]/div[5]/div[1]')))

    time.sleep(7)
    container_timezon = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, '//*[@id="results"]/div[3]/div[5]/div[1]')))
    print(" FNGERPRINTING ......... ",end='')
    print(container_timezon.text)
    time.sleep(7)
    container_webgl = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, '//*[@id="results"]/div[3]/div[11]/div[1]')))

    container_1 = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, '//*[@id="results"]/div[3]/div[10]/div[1]')))


    #print(driver.current_url) //*[@id="results"]/div[3]/div[5]/div[1]

    print("CAVNAS FNGERPRINTING ......... ",end='')
    print(container_1.text)
    print("WEB-GL FNGERPRINTING ......... ",end='')
    print(container_webgl.text)
    #//*[@id="results"]/div[3]/div[5]/div[1]
    driver.get("https://browserleaks.com/webgl")
    #input()
    
    # input()https://browserleaks.com/canvas
    return startY, height0
####################################################################################################""

def lets_play(serv,ops):

	try:
		print("OPEN DISPLAY  WEB-SITE ......... ",end='')
		#display = Display(visible=1, size=(width,height), use_xauth=False).start()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))


	except Exception as error:
		print(str(error))
		exit(0)
	
	print("OPEN AND VISITE WEB-SITE ...... ",end='')
	time.sleep(1)
	time.sleep(1)
	try:
		
		#print(ops)
		driver = webdriver.Firefox(service=serv, options=ops)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		extension_path="/root/moya/SEL_LAB/spoofHeadless-master/canvasblocker44b.xpi"
		#extension_path="/root/OUOIO/SEL_LAB/spoofHeadless-master/extension.xpi"
		extension_help_path="/root/moya/SEL_LAB/spoofHeadless-master/extension.xpi"
		#driver.install_addon(extension_help_path, True)
		#driver.install_addon(extension_path, True)

		driver.set_page_load_timeout(79)
		latitude = 42.1408845
		longitude = -72.5033907
		accuracy = 100
		#driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {"latitude": latitude,"longitude":longitude,"accuracy": accuracy})
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		#
		action = ActionChains(driver)
		#print(driver.execute_script("return navigator.userAgent;"))
		#https://coveryourtracks.eff.org/ https://browserleaks.com/webgl
		#driver.get("https://browserleaks.com/webrtc#howto-disable-webrtc")https://browserleaks.com/canvas
		driver.get("https://coveryourtracks.eff.org/")
		#driver.get("https://browserleaks.com/webgl")

		driver.maximize_window()
		time.sleep(2)
		product_page(driver)
		weak_info(driver)
		#check_web(driver)
		#input()
		###############
		
		# startY, height0 = product_page(driver)
		# print(str(height0))
		# print(str(startY))
		#pyautogui.moveTo(startY, height0)

	except Exception as error:
		print(str(error))
#####################################################################################################
def weak_info(driver):
	try:
		driver.get("https://browserleaks.com/canvas")
		container_timezon = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, '//*[@id="crc"]')))
		print("CAVNAS FNGERPRINTING ......... ",end='')
		print(container_timezon.text)
		pass
	except Exception as e:
		print(str(e))
		raise e
#####################################################################################################
def check_web(driver ):
	print("###########################CHECK WEB DRIVER  CHECK#################################")
	print("CHECK WEB DRIVER  CHECK .....")
	driver.maximize_window()
	try:
		driver.get("https://serene-keller-a6f116.netlify.app/index.html")
		time.sleep(20)
		driver.execute_script("window.open('');")
		time.sleep(1)
		driver.switch_to.window(driver.window_handles[1])
		time.sleep(1)
		driver.get("https://serene-keller-a6f116.netlify.app/index.html")
		time.sleep(20)
		
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[2])
		driver.get("https://cocky-bose-de943a.netlify.app/index.html")
		driver.maximize_window()# display.start()
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[3])
		print("Display Stop !!!")
		#my_vpn()
	except Exception as a:
		print("something wrong   starter"+str(a))
	try:
		#print("OPEN URL  A-ADS CHECK .....",end='')
		print("MY BTTTC !!!!!!", end='')
		driver.get("https://serene-keller-a6f116.netlify.app/index.html")
		time.sleep(8)
		maain_button=WebDriverWait(driver, 19).until(EC.presence_of_element_located((By.ID, 'rightbox')))
		time.sleep(3)
		#maain_button.send_keys(Keys.RETURN)
		time.sleep(5)
		maain_button.click()
		time.sleep(40)
		print("OK !!!!!")
		#https://app.netlify.com/sites/flamboyant-kalam-54b358
	except Exception as a:
		print("something wrong check web issu drive "+str(a))
		##try:
			##driver.quit()
			#display.stop()
		##except:
			##pass
		##driver.close()
		pass
		#input('endddddddddddddd')
#################################################################################################################
def starting_tasks():
	try:
		stage_1()### CLEAR
		time.sleep(2)
		#
		#init_fire()
		#my_vpn ()

		serv,ops=build_driver()
		#build_driver()###### BUILDING DRIVER QQQ
		display = Display(visible=0, size=(width,height), use_xauth=False).start()
		lets_play(serv,ops)
		display.stop()
		time.sleep(2)
		init_fire()


	except Exception as error:
		print (str(error))
starting_tasks()
# iip()
# iip()