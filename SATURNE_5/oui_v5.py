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

###########global urls_BVB
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
	random_vpn=random.choice(os.listdir(cnf_bvb.p_vpn_g))
	os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	time.sleep(3)
	print ("OK !!!!!")
	os.system("rm -rf /var/log/openvpn/openvpn.log")
	c_ip=iip()
	print(random_vpn)
	path = cnf_bvb.p_vpn_g+random_vpn
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
		#fp.set_preference("http.response.timeout",95)
		fp.set_preference("general.useragent.override",user_agent)
		fp.set_preference('webdriver.load.strategy','unstable')
		fp.set_preference("modifyheaders.headers.count", 2)
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference("modifyheaders.headers.action0", "Add")
		fp.set_preference("modifyheaders.headers.name0", "x-msisdn")
		fp.set_preference("dom.push.enabled", False)
		fp.set_preference("media.peerconnection.enabled", False)

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


#####################################




def lets_play(serv,ops):

	try:
		print("OPEN DISPLAY  WEB-SITE ......... ",end='')
		display = Display(visible=1, size=(width,height)).start()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))


	except Exception as error:
		print(str(error))
		exit(0)
	
	print("OPEN AND VISITE WEB-SITE ...... ",end='')
	time.sleep(1)
	try:
		
		#print(ops)
		driver = webdriver.Firefox(service=serv, options=ops)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		driver.set_page_load_timeout(79)
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		#
		action = ActionChains(driver)
		#print(driver.execute_script("return navigator.userAgent;"))
		driver.get(urls_BVB)
		driver.maximize_window()
		time.sleep(2)
		###############


	except Exception as error:
		print(str(error))
###################################################################################################
	
	print("CHECK NOTIFICATION  ..... : ",end='')
	try:
		WebDriverWait(driver, 3).until(EC.alert_is_present(),'Timed out waiting for PA creation '+'confirmation popup to appear.')
		print(emoji.emojize(" FOUD NOTIFICATION "' :check_mark_button: :alien:'))
		pass
	except Exception as e:
		print(emoji.emojize("NOT FOUND  "' :check_mark_button: :alien:'))
		#raise e
		pass
	print("Click GO TO CAPTCHA  PAGE ..... : ",end='')	
	try:
		#######Click GO TO CAPTCHA
		#etLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'getLink')))
		#
		#                   SCROLLIG DOWN

		here_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'here')))
		time.sleep(1)
		try:
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
		except Exception as e:
			print(str(e))
			#raise e
		time.sleep(2)
		#here_button.send_keys(Keys.PAGE_DOWN)
		
		action.move_to_element(here_button).click().perform()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		######################################################################################################
		print(len(driver.window_handles))
		driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
		print("Length of Driver = ", driver_len)
##############################################################################################################

		

####################################################################################################################
		
		time.sleep(3)
		rain_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.container')))
		time.sleep(1)
		#rain_button.send_keys(Keys.TAB)
		try:
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);window.scrollTo(0, document.body.scrollHeight/4.5);")
		except Exception as e:
			print(str(e))
			#raise e
		time.sleep(1)
		#//*[@id="captcha"]
		time.sleep(2)
		#rain_button.send_keys(Keys.TAB)
		
		recaptcha_ok=WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,'//*[@id="captcha"]')))
		#recaptcha_ok.send_keys(Keys.PAGE_UP)
		number_fra=len(driver.find_elements_by_tag_name("iframe"))
		print(number_fra)
		
		iframes=driver.find_elements_by_tag_name("iframe")
		for index, iframe in enumerate(iframes):
			print("SWITCH TO IFRAME "+ str(index) + " : ",end='')
			driver.switch_to.frame(index)
			#print("  OK !!!!!!", end='')
			time.sleep(3)
			try:
				#print("Button AUDIO CHECK CAPATCHA  ... : ",end='')#Get Link
				main_button=WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.fbc-button-audio.fbc-button')))
				#main_button.send_keys(Keys.RETURN)
				
				time.sleep(3)
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")

				action = ActionChains(driver)
				action.move_to_element(main_button).click().perform()
				#print("Button AUDIO CHECK CAPATCHA OK !!!!")#Get Link
				driver.switch_to.parent_frame()
				time.sleep(3)
				#print("OK  Back To Frames  !!!")#Get Link
				print("Button AUDIO CHECK CAPATCHA OK !!!!")#Get Link
				driver.switch_to.parent_frame()
				break
			except  Exception as b :
				print(" NOT Found ")#Get Link
				driver.switch_to.parent_frame()
				pass
		time.sleep(2)
		driver.switch_to.parent_frame()
		time.sleep(3)
		print("captcha DONNE GO TO SUBMIT BUTTUN")
		
		try:
			submit_button=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-main')))
			time.sleep(2)
			#submit_button.click()
			submit_button.send_keys(Keys.TAB)
			action = ActionChains(driver)
			action.move_to_element(submit_button).click().perform()
			time.sleep(3)
			print("  Submit OK !!!")#Get Link
		except  Exception as b :
			print(b)
			print("NOT Found SUBMI !!!")#Get Link
		#driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
		#main_button=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.fbc-button-audio.fbc-button')))
		#action.move_to_element(main_button).click().perform()

		time.sleep(6)
		main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		time.sleep(6)
		main_button.send_keys(Keys.TAB)
		time.sleep(3)
		action = ActionChains(driver)
		action.move_to_element(main_button).click().perform()	
		#main_button.click()
		print("button  I'M HUMMEN BEEN !!!")#Get Link
		time.sleep(2)
		try:
			main_button=WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		except Exception as e:
			pass
		#input()
		#print("captcha FOUD")
		driver_len = len(driver.window_handles)
		if driver_len > 1:
			driver.switch_to.window(driver.window_handles[1])
			time.sleep(5)
			try:
				main_button=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'btn-main')))
			except:
				pass
			driver.close()
			time.sleep(3)
			driver.switch_to.window(driver.window_handles[0])
			time.sleep(3)
			try:
				main_button=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'btn-main')))
			except:
				pass

			#for i in range(driver_len - 1, 0, -1):				
			#	driver.switch_to.window(driver.window_handles[i])
			#	time.sleep(6)
				#driver.close()
			#	print("Closed Tab No. ", i)
			#driver.switch_to.window(driver.window_handles[0])
		else:
			print("Found only Single tab.")

		#input()

		#driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
		#driver.switch_to_frame(recaptcha_ok)

		#action.move_to_element(here_button).click().perform()
		#print("captcha FOUD")


		#input()
	except Exception as error:
		print(str(error))









	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(3)
	except:
		pass
	try:
		print("Close Display ...... ",end='')
		display.stop()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except:
		pass


#####################################




def stage_1():
	try:
		#print (urls_BVB)
		os.system("rm -rf /tmp/*") 
		os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+urls_BVB+' :check_mark_button: :alien:'))
		print(emoji.emojize("Resolution : "+random_display_chose+' :check_mark_button: :alien:'))
		#####TO DO PRINT ONLY THE SYSTEM
		#print(width+"x"+height)
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")

	except Exception as error:
		print (str(error))




#################################"MAIN STARTING"##############################

def starting_tasks():
	try:
		stage_1()### CLEAR
		my_vpn ()

		serv,ops=build_driver()
		#build_driver()###### BUILDING DRIVER
		lets_play(serv,ops)

	except Exception as error:
		print (str(error))
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

starting_tasks()
#starting_tasks()