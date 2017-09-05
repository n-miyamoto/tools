# -*- coding: utf-8 -*-
from selenium import webdriver
import sys
import config 


pi = config.personal_info

MAIL_ADDR 		= pi.mail_addr
PHONE 			= pi.phone 
LAST_NAME 		= pi.last_name
FIRST_NAME 		= pi.first_name
LAST_NAME_KANA 	= pi.last_name_kana
FIRST_NAME_KANA = pi.first_name_kana
ADDR_PRFCTR 	= pi.addr_prf
ADDR_DSTRCT 	= pi.addr_dstrct
ADDR_CITY   	= pi.addr_city
ADDR_CHOME  	= pi.addr_chome
ADDR_BANCHI 	= pi.addr_banchi
ADDR_GOU    	= pi.addr_gou
ADDR_ROOM   	= pi.addr_room

DATE = "20170901"	
TIME = 3

TIME_CODE = [
	"20050",	#希望なし
	"20100",	#午前中
	"20300",	#14~16
	"20400",	#16~18	
	"20500",	#18~20
	"20550"		#19~21
] 

#imput 
print(">>>Please input slip number. e.g) 304069707686")
MY_SLIP_NUMBER = input()
print("Slip number is " + MY_SLIP_NUMBER)

print(">>>Please input date. e.g)20170902")
DATE = input()
print("Date is " + DATE)

print(">>>Please input time code. e.g)3")
TIME = input()
print("TIME code is " + TIME)
TIME = int(TIME)


###1st page###
URL="https://syuhai.kuronekoyamato.co.jp/simple_saihai/SERVICE_MENU"
#open and access web page.
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(URL)
print(driver.current_url)
#input slip number (denpyo bango) and go to next page
slip_number_box_path ='//*[@id="denpyo"]'
next_button_path = '//*[@id="BTN_NEXT"]'

slip_number_box = driver.find_element_by_xpath(slip_number_box_path)
next_button = driver.find_element_by_xpath(next_button_path)

slip_number_box.send_keys(MY_SLIP_NUMBER)
#goto next page
next_button.click()

###2nd page###

#input data and other information
data_box_path = '//*[@id="saihaiKiboubi"]'
time_box_path = '//*[@id="saihaiKiboujikantai"]'
phone_a_path  = '//*[@name="cstmrTel1"]'
phone_b_path  = '//*[@name="cstmrTel2"]'
phone_c_path  = '//*[@name="cstmrTel3"]'

last_name_path       = '//*[@id="sei"]'
first_name_path      = '//*[@id="mei"]'
last_kana_name_path  = '//*[@id="seikana"]'
first_kana_name_path = '//*[@id="meikana"]'

mail_box_path = '//*[@name="cstmrMailAddr"]'
mail_box_cnfrm_path = '//*[@name="confirmMailAddr"]'

next_button_path = '//*[@id="BTN_NEXT"]'

#data_box = driver.find_element_by_xpath(data_box_path)
#time_box = driver.find_element_by_xpath(time_box_path)

phone_a = driver.find_element_by_xpath(phone_a_path)
phone_b = driver.find_element_by_xpath(phone_b_path)
phone_c = driver.find_element_by_xpath(phone_c_path)

last_name = driver.find_element_by_xpath(last_name_path)
first_name= driver.find_element_by_xpath(first_name_path)
last_kana_name = driver.find_element_by_xpath(last_kana_name_path)
first_kana_name= driver.find_element_by_xpath(first_kana_name_path)

mail_box = driver.find_element_by_xpath(mail_box_path)
mail_box_cnfrm = driver.find_element_by_xpath(mail_box_cnfrm_path)

next_button = driver.find_element_by_xpath(next_button_path)

#input phone number
data_box_path = '//*[@value="' + DATE + '"]'
data_box = driver.find_element_by_xpath(data_box_path)
data_box.click()

time_box_path =  '//*[@value="' + TIME_CODE[TIME] + '"]'
time_box = driver.find_element_by_xpath(time_box_path)
time_box.click()


phone = PHONE.split('-')
phone_a.send_keys(phone[0])
phone_b.send_keys(phone[1])
phone_c.send_keys(phone[2])

#input name
last_name.send_keys(LAST_NAME)
first_name.send_keys(FIRST_NAME)
last_kana_name.send_keys(LAST_NAME_KANA)
first_kana_name.send_keys(FIRST_NAME_KANA)

#input mail
mail_box.send_keys(MAIL_ADDR)
mail_box_cnfrm.send_keys(MAIL_ADDR)

#goto next page
next_button.click()

###3rd page###
prfctr_link=driver.find_element_by_link_text(ADDR_PRFCTR)
prfctr_link.click()

###4th page###
dstrct_link = driver.find_element_by_link_text(ADDR_DSTRCT)
dstrct_link.click()

###5th page###
dstrct_link = driver.find_element_by_link_text(ADDR_CITY)
dstrct_link.click()

###6th page###
dstrct_link = driver.find_element_by_link_text(ADDR_CHOME)
dstrct_link.click()

banchi_path = '//*[@id="contentsIn"]/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input[1]'
gou_path   = '//*[@id="contentsIn"]/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input[2]'
build_path = '//*[@id="contentsIn"]/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input'
next_button_path = '//*[@id="contentsIn"]/form/div/p/input[2]'

banchi_box = driver.find_element_by_xpath(banchi_path)
gou_box   = driver.find_element_by_xpath(gou_path)
build_box = driver.find_element_by_xpath(build_path)
next_button=driver.find_element_by_xpath(next_button_path)

banchi_box.send_keys(ADDR_BANCHI)
gou_box.send_keys(ADDR_GOU)
build_box.send_keys(ADDR_ROOM)
next_button.click()

###7th page###
next_button_path = '//*[@id="contentsIn"]/div[6]/p/input[2]'
next_button =driver.find_element_by_xpath(next_button_path)
next_button.click()
###check
SUCCESS_URL = 'https://syuhai.kuronekoyamato.co.jp/simple_saihai/COMPLETE'
url = driver.current_url

if(url == SUCCESS_URL):
	print("Redelivary successed!!!")
else:
	print("Failed!!!")