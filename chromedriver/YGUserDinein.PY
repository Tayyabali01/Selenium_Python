from xml.dom.minidom import Element
from selenium import webdriver
import selenium
import cv2
import pyautogui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
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
import requests
import numpy as np
import os
import base64
import re
import datetime
import random
import time

print(selenium.__version__)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get('https://devuser.yallagrub.com/')
WAKHA_AlBrasha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div[contains(@class,'mx-4')]/div[contains(@class,'flex flex-col md:flex-row md:flex-wrap')]/div[1]/div[1]/div[1]")))
# click the element
WAKHA_AlBrasha.click()
time.sleep(2)
# enter text

Statersbolanibonjon_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Fried eggplants covered with fresh cooked tomatoes, onion & yogurt sauce. Served with bread & chutni (Spicy dip)']")))
Statersbolanibonjon_btn .click()
time.sleep(2)

Select1_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex justify-between items-center menu-quantity-items']//div[3]//*[name()='svg']")))
Select1_btn.click()
time.sleep(2)
#Email_Text.send_keys("tayyab2@mailinator.com")

Addtocart_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex w-full bg-pink text-white py-3 px-4 rounded justify-between']")))
Addtocart_btn.click()
time.sleep(2)
#Password_Text.send_keys("Ali12345")

# Scroll down the last section of screen
#driver.execute_script("window.scrollTo(0.5, document.body.scrollHeight);")

# Scroll down to the half page
driver.execute_script("window.scrollTo(0, (window.scrollY + window.innerHeight) / 2);")
time.sleep(2)

AddTip_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='+5 AED']")))
AddTip_btn.click()
time.sleep(2)

LetsPlanYourOrder_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'bg-pink my-5 py-4 w-full text-white rounded-md')]")))
LetsPlanYourOrder_btn .click()
time.sleep(2)

#Create Reservation Screen
NoOfGuests_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='username']")))
NoOfGuests_textbox .click()
NoOfGuests_textbox .clear()
NoOfGuests_textbox .send_keys("10")
time.sleep(2)



#SelectDate
SelectDate_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text-xs']")))
SelectDate_textbox .click()

#To get automatic date for today
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

# Build the aria-label string
aria_label = f"Choose {day_of_week}, {today.strftime('%B')} {day}{ordinal_indicator}, {today.year}"

# Build the XPath with the dynamically obtained date
xpath = f"//div[contains(@aria-label, '{aria_label}')]"

# Click on the button for today's date
Selecttodaydate_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
#print(xpath)
Selecttodaydate_btn.click()


# Selecttodaydate_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@aria-label,'Choose Thursday, June 8th, 2023')]")))
# Selecttodaydate_btn .click()

time.sleep(2)

#Select Preffered time
SelectPrefferedtime_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Select Preferred Time')]")))
SelectPrefferedtime_textbox .click()
time.sleep(2)

# Locate the dropdown options and select the option by index
options = driver.find_elements(By.XPATH, "//li[contains(@class, 'cursor-default')]")
index = 0  # Index of the option to be selected (assuming '17:45' is the first option)
options[index].click()

time.sleep(5)
# SelectPrefferedtime1st_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ml-3 block truncate'][normalize-space()='17:45']")))
# SelectPrefferedtime1st_btn.click()


#Select 2nd Time Slot
Select2ndTimeSlot_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='headlessui-listbox-button-:r8:']//span[@class='flex items-center']")))
Select2ndTimeSlot_textbox .click()
# Locate the dropdown options and select the option by index
options = driver.find_elements(By.XPATH, "//li[contains(@class, 'cursor-default')]")
index = 0  # Index of the option to be selected (assuming '17:45' is the first option)
options[index].click()

time.sleep(5)
# Select2ndTimeSlot_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ml-3 block truncate'][normalize-space()='18:00']")))
# Select2ndTimeSlot_btn .click()
# time.sleep(2)

#Select 3rd Time Slot

Select3rdTimeSlot_textbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Time Slot Option')]")))
Select3rdTimeSlot_textbox .click()
# Locate the dropdown options and select the option by index
options = driver.find_elements(By.XPATH, "//li[contains(@class, 'cursor-default')]")
index = 0  # Index of the option to be selected (assuming '17:45' is the first option)
options[index].click()

time.sleep(5)
# Select3rdTimeSlot_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='18:15']")))
# Select3rdTimeSlot_btn .click()
# time.sleep(2)

NEXT_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex items-center justify-center']")))
NEXT_btn .click()
time.sleep(2)
#Your Information
FullName_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='clientFullName']")))
time.sleep(2)
FullName_Textfield .click()
FullName_Textfield .send_keys("Tayyab ali")

Email_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder=' ']")))
Email_Textfield.click()
time.sleep(2)
Email_Textfield.send_keys("tayyabalisa123@gmail.com")

PhoneNumber_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='1 (702) 123-4567']")))
PhoneNumber_Textfield.click()
time.sleep(2)
PhoneNumber_Textfield.send_keys("7373474775")

Checkout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Checkout']")))
Checkout_btn.click()
time.sleep(10)

EnterOTP_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='otp1']")))
EnterOTP_Textfield.click()
EnterOTP_Textfield.send_keys("55690")

Verify_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Verify']")))
Verify_btn.click()
time.sleep(2)

#Debit Card Information 


iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^="__privateStripeFrame"]')))

# Switch to the iframe
driver.switch_to.frame(iframe)

# Wait for the input field to be clickable and enter the card number
CardNumbers_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="number"]')))
CardNumbers_Textfield.click()
CardNumbers_Textfield.send_keys("4242 4242 4242 4242")
time.sleep(2)
# Switch back to the main content
driver.switch_to.default_content()


iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^="__privateStripeFrame"]')))

# Switch to the iframe
driver.switch_to.frame(iframe)

Expiration_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="expiry"]')))
Expiration_Textfield.click()
Expiration_Textfield.send_keys("1256")
time.sleep(2)

driver.switch_to.default_content()

iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^="__privateStripeFrame"]')))

# Switch to the iframe
driver.switch_to.frame(iframe)

CVC_Textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="cvc"]')))
CVC_Textfield.click()
CVC_Textfield.send_keys("776")
time.sleep(2)

driver.switch_to.default_content()

PayNow_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='button-text']")))
PayNow_btn.click()
time.sleep(2)

TrackOrder_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Track order']")))
TrackOrder_btn.click() 
time.sleep(2)

driver.execute_script("window.scrollTo(0, (window.scrollY + window.innerHeight) / 2);")

time.sleep(2)

order_number_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Order Number")]/following-sibling::div[@class="h7 font-semibold"]')
order_number = order_number_element.text

order_type_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Order Type")]/following-sibling::div[@class="h7 font-semibold"]')
order_type = order_type_element.text

guest_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Guests")]/following-sibling::div[@class="h7 font-semibold"]')
guest = guest_element.text

Table_No_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Table No")]/following-sibling::div[@class="h7 font-semibold"]')
Table_No = Table_No_element.text

Date_type_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Date")]/following-sibling::div[@class="h7 font-semibold"]')
Date_type = Date_type_element.text

Time_type_element = driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Time")]/following-sibling::div[@class="h7 font-semibold"]')
Time_type = Time_type_element.text

print("Order Number:", order_number)
print("Order Type:", order_type)
print("Guest:", guest)
print("Table_No:", Table_No)
print("Date_type:", Date_type)
print("Time_type:", Time_type)






