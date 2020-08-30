# 27-08-2020 Switched to firefox
#	Issues encountered:
#				1. Tab switching problem : Added delay after click on '7/12 paha.'
#	
#	Features awaiting:
#				1. Multiple 7/12 facility				

from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui as gui
from win10toast import ToastNotifier 
import base64
import time
from time import sleep
from random import randint


#def Closeprevtab():
selectedTalXpath = "//*[@id='talSelect']/option[4]"
#
selectedSurveyXpath = "//*[@id='rbsryno']"
selectedSurveyNo = 416

# Main Form
'''
def mainForm():
	from tkinter import *
	from tkinter import ttk
	root = Tk()
	root.title("Automatic 7/12 Download [ Created by Ashish Ghadoje 9284183715")
	root.geometry('450x450')
	root.configure(background = "grey")

	def show():
		myLabel = Label(root, text = clicked.get()).pack()
	clicked = StringVar() 
	clicked.set("Kanmandale")
	drop = OptionMenu(root, clicked, "Kanmandale", "Sherisalayban", "Kundane", "Puri")
	drop.pack()
	myButton = Button(root, text = "Show selection", command=show ).pack()
	root.mainloop()
'''
#############################################################
def randomMobile():
	n = 9
	range_start = 10**(n-1)
	range_end = (10**n)-1
	value = randint(range_start, range_end)
	tenDigitNumber = '8'+str(value)
	return tenDigitNumber

def UtaraOpen(selectedVilXpath, selectedSurveyNo):
	driver = webdriver.Firefox()
	driver.get("http://bhulekh.mahabhumi.gov.in")
	dist= driver.find_element_by_xpath("//*[@id='list']/option[5]")
	dist.click()
	go = driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_Panel1']/p[2]/input")
	go.click()
	driver.close()
	driver.switch_to.window(driver.window_handles[0]) # Needed even if previous tab is closed.



	ot = time.time()
	try:
	    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "distSelect")))
	    print('Element found successfully:  District.')
	except:
	    print('Not found :  District.')
	ct = time.time()

	
	#print(ct-ot)
	#print(driver.current_url)
	XPATH = "//*[@id='distSelect']/option[5]"
	try:
	    dist2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, XPATH))).click()
	    print('Element found successfully:  Taluka')
	except:
	    print('Not found :  Taluka.1')


	'''try:
	    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "talSelect"))).click()
	    print('Element found successfully:  Taluka')
	except:
	    print('Not found :  Taluka.2') '''
	
	sleep(1)
	taluka = driver.find_element_by_xpath(selectedTalXpath).click()

	try:
	    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "vilSelect")))
	    print('Element found successfully:  Village')
	except:
	    print('Not found :  Village.')
	sleep(1)
	village = driver.find_element_by_xpath(selectedVilXpath).click()

	try:
	    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "rbsryno"))).click()
	    print('Element found successfully:  Survey no')
	except:
	    print('Not found :  Survey No.')
	
	village = driver.find_element_by_xpath(selectedSurveyXpath).click()

	surveyFieldXPATH = "//*[@id='aspnetForm']/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[1]/td[1]/input[1]"

	try:
	    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, surveyFieldXPATH))).click()
	    print('Element found successfully:  Survey no field')
	except:
	    print('Not found :  Survey no field.')
	
	surveyField = driver.find_element_by_xpath(surveyFieldXPATH)
	# For loop
	for n in selectedSurveyNo:
		surveyField.clear()
		#print(int(selectedSurveyNo[n]))
		surveyField.send_keys(str(n))
		searchButtonXPATH = "//*[@id='aspnetForm']/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[1]/td[2]/input"
		searchButton = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,searchButtonXPATH))).click()
		sleep(1)
		XPATH = "//*[@id='aspnetForm']/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[3]/td/select[1]" # Survey No. drop down list
		
		select_element = Select(driver.find_element_by_xpath(XPATH)) #
		

		select_element.select_by_value('string:' + str(n) +'########') # Selects Survey number from dropdown list
		sleep(0.5)

		print(randomMobile())
		mobile = driver.find_element_by_xpath("//*[@id='aspnetForm']/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[4]/td/div/input")
		mobile.send_keys(randomMobile())
		sleep(0.5)

		main_window = driver.current_window_handle
		#print("Window Handle name: old ", driver.current_window_handle)

		XPATH = "//*[@id='aspnetForm']/div[4]/div/div/div[3]/div/div[4]/table/tbody/tr[5]/td/input[1]" # '7/12 Paha Xpath'
		try:
		    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, XPATH))).click()
		    print('Element found successfully:  7/12 Paha Button')
		except:
		    print('Button Not found (button) :  7/12 Paha.')
		sleep(1)
		driver.switch_to.window(driver.window_handles[1])
		x = ToastNotifier()
		x.show_toast("Please enter Captcha", "Robot calling", duration = 3)

		captchaB64 = driver.find_element_by_id("Image3").get_attribute("src")
		img = bytes(captchaB64, 'utf-8')
		import base64
		filename = "Utara No. " + str(n)+".png"
		with open(filename, "wb") as fh:
			fh.write(base64.decodebytes(img[22:]))
		
		driver.switch_to.window(driver.window_handles[0])

	return filename

'''
def CaptchaCapture():
	captchaB64 = driver.find_element_by_id("Image3").get_attribute("src")
	img = bytes(captchaB64, 'utf-8')
	import base64
	a = 1
	filename = "captcha"+ a + ".png"
	with open(filename, "wb") as fh:
		fh.write(base64.decodebytes(img[22:]))
		a = a+1	
		'''

		
		

