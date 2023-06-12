from xml.dom.minidom import Element
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import datetime
import random
import time

print(selenium.__version__)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get('https://devbranch.yallagrub.com/')

#Login Wakha Albarsha
LoginEmail_textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
LoginEmail_textfield.click()
LoginEmail_textfield.send_keys("wakha_albarsha@gmail.com")
time.sleep(2)

Password_textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
Password_textfield.click()
Password_textfield.send_keys("12341234")
time.sleep(2)

rememberMe_Checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='rememberMe']")))
rememberMe_Checkbox.click()
time.sleep(2)

Login_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Login_Button.click()
time.sleep(2)

#Orders 
PendingOrder_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='Pending']")))
PendingOrder_button.click()
time.sleep(2)



# Click on the first pending order in the dialog box
FirstOrderPending_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstOrderPending_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)


# Find and print the customer details using XPath
ordernumber_element = driver.find_element_by_xpath("//div[@class='modal-body']//div[contains(text(),'Order#')]")
ordernumber = ordernumber_element.text 
expectedtime_element= driver.find_element_by_xpath("//div[@class='modal-body']//div[contains(text(),'Expected Time')]")
expectedtime = expectedtime_element.text
customername_element = driver.find_element_by_xpath("//div[@class='modal-body']//div[@class='fs-8 fw-600 text-gray-3']")
customername= customername_element.text
customerphone_element = driver.find_element_by_xpath("//div[@class='modal-body']//div[@class='fs-7 text-gray-5']")
customerphone= customerphone_element.text

print("Order Number:", ordernumber)
print("Expected Time:", expectedtime)
print("Customer Name:", customername)
print("Customer Phone:", customerphone)
# Get the current time
#Testing 
current_time = datetime.datetime.now().time()
print('hello', current_time)

# To get automatic date for today
def get_ordinal_indicator(day):
    if 11 <= day <= 13:
        return 'th'
    else:
        last_digit = day % 10
        if last_digit == 1:
            return 'st'
        elif last_digit == 2:
            return 'nd'
        elif last_digit == 3:
            return 'rd'
        else:
            return 'th'

# Get today's date
today = datetime.date.today()
# Get the day of the week and ordinal indicator
day_of_week = today.strftime("%A")
day = today.day
ordinal_indicator = get_ordinal_indicator(day)



# Subtract 1 hour from the current time
target_datetime = datetime.datetime.combine(datetime.date.today(), current_time) - datetime.timedelta(hours=1)
target_time = target_datetime.time()

print("Target time:", target_time)


# Compare the current time with the target time
if current_time > target_time:
    SelectFirstPrefferedtime_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='time1']"))
    )
    SelectFirstPrefferedtime_checkbox.click()
    time.sleep(2)

    SelectTable_dialogbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//select[@id='tableNumbers']"))
    )
    time.sleep(5)

    select = Select(SelectTable_dialogbox)
    desired_option = "02"  # Replace with the value of the option you want to select
    select.select_by_value(desired_option)
    time.sleep(3)

 #Code for canceling the order
    CancelOrder_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel Order']")))
    CancelOrder_btn.click()
    time.sleep(3)
    CancelOrderSuccess_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel and Refund']")))
    CancelOrderSuccess_btn.click()
    print("order cancel successfully", CancelOrderSuccess_btn)
    time.sleep(5)

#Refund screen 
    YesFullRefund_Checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='fullRefund']")))
    YesFullRefund_Checkbox.click()
   
    SelectReason1_Checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='reason1']")))
    SelectReason1_Checkbox.click()

    Refund_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Refund']")))
    Refund_btn.click()

else:
#Code for Accepting the order
    SelectFirstPrefferedtime_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='time1']"))
    )
    SelectFirstPrefferedtime_checkbox.click()
    time.sleep(2)

    SelectTable_dialogbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//select[@id='tableNumbers']"))
    )
    time.sleep(3)

    select = Select(SelectTable_dialogbox)
    desired_option = "02"  # Replace with the value of the option you want to select
    select.select_by_value(desired_option)

    AcceptOrder_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept Order']"))
    )
    AcceptOrder_btn.click()
    time.sleep(100)









