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
import subprocess

print(selenium.__version__)

class UserApp_SelectItem:
    def __init__(self, driver):
        self.driver = driver 
    
    def WAKHA_AlBrasha(self):
        WAKHA_AlBrasha = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div[contains(@class,'mx-4')]/div[contains(@class,'flex flex-col md:flex-row md:flex-wrap')]/div[1]/div[1]/div[1]")))
        WAKHA_AlBrasha.click()
        time.sleep(2)
    def Breadsitem_btn(self):
        Breadsitem_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Breads']")))
        Breadsitem_btn.click()
        time.sleep(2)
    def BlackseedNaan_item(self):
        BlackseedNaan_item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='Blackseed Naan']")))
        BlackseedNaan_item.click()
        time.sleep(2)
    def Select1_btn(self):
        Select1_btn= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex justify-between items-center menu-quantity-items']//div[3]//*[name()='svg']")))
        Select1_btn.click()
        time.sleep(2)
    def Addtocart_btn(self):
        Addtocart_btn= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex w-full bg-pink text-white py-3 px-4 rounded justify-between']")))
        Addtocart_btn.click()
        time.sleep(3)
    def ShinwariBBQ_btn(self):
        ShinwariBBQ_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Shinwari BBQ']")))
        ShinwariBBQ_btn.click()
        time.sleep(2)
    def CHICKENCHARGHA_item(self):
        CHICKENCHARGHA_item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='CHICKEN CHARGHA']")))
        CHICKENCHARGHA_item.click()
        time.sleep(2)
    def Select1_btn(self):
        Select1_btn= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex justify-between items-center menu-quantity-items']//div[3]//*[name()='svg']")))
        Select1_btn.click()
        actions = ActionChains(self.driver)
        actions.double_click(Select1_btn).perform()
    def Addtocart_btn(self):
        Addtocart_btn= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex w-full bg-pink text-white py-3 px-4 rounded justify-between']")))
        Addtocart_btn.click()
        # Scroll down to the half page
        self.driver.execute_script("window.scrollTo(0, (window.scrollY + window.innerHeight) / 2);")
        time.sleep(2)
    def AddTip_btn(self):
        AddTip_btn= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='+5 AED']")))
        AddTip_btn.click()
        time.sleep(2)
    def LetsPlanYourOrder_btn(self):
        LetsPlanYourOrder_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'bg-pink my-5 py-4 w-full text-white rounded-md')]")))
        LetsPlanYourOrder_btn .click()
        time.sleep(5)

class Create_Reservation:
    def __init__(self, driver):
        self.driver = driver

    def enter_no_of_guests(self, num_guests):
        no_of_guests_textbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='username']")))
        no_of_guests_textbox .click()
        no_of_guests_textbox .clear()
        no_of_guests_textbox .send_keys(str(num_guests))
        time.sleep(2)

    def SelectDate_textbox(self):
        SelectDate_textbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text-xs']")))
        SelectDate_textbox.click()
        time.sleep(2)

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
        Selecttodaydate_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        Selecttodaydate_btn.click()
        time.sleep(3)
    def SelectPrefferedtime_textbox(self):
        SelectPrefferedtime_textbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Select Preferred Time')]")))
        SelectPrefferedtime_textbox .click()
        # Locate the dropdown options and select the option by index
        options = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'cursor-default')]")
        index = 0  # Index of the option to be selected (assuming '17:45' is the first option)
        options[index].click()
        time.sleep(3)
    def Select2ndTimeSlot_textbox(self):
        Select2ndTimeSlot_textbox= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Time Slot Option')]")))
        Select2ndTimeSlot_textbox .click()
        # Locate the dropdown options and select the option by index
        options = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'cursor-default')]")
        index = 0  # Index of the option to be selected (assuming '17:45' is the first option)
        options[index].click()
        time.sleep(3)

    def Select3rdTimeSlot_textbox(self):
        Select3rdTimeSlot_textbox= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Time Slot Option')]")))
        Select3rdTimeSlot_textbox .click()
        # Locate the dropdown options and select the option by index
        options = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'cursor-default')]")
        index = 0  # Index of the option to be selected (assuming '17:45' is the first option)
        options[index].click()
        time.sleep(3)
    def Next_btn(self):
        NEXT_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex items-center justify-center']")))
        NEXT_btn .click()
        time.sleep(5)
class Personal_Information:
    def __init__(self, driver):
        self.driver = driver

    def FullName_Textfield(self, Name_guests):
        FullName_Textfield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='clientFullName']")))
        FullName_Textfield .click()
        FullName_Textfield .clear()
        FullName_Textfield .send_keys(str(Name_guests))
        time.sleep(2)

    def Email_Textfield(self, Email_guests):
        Email_Textfield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder=' ']")))
        Email_Textfield .click()
        Email_Textfield .clear()
        Email_Textfield .send_keys(str(Email_guests))
        time.sleep(2)

    def PhoneNumber_Textfield(self, PhoneNumber_guests):
        PhoneNumber_Textfield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='1 (702) 123-4567']")))
        PhoneNumber_Textfield .click()
        PhoneNumber_Textfield .clear()
        PhoneNumber_Textfield .send_keys(str(PhoneNumber_guests))
        time.sleep(2)

    def Checkout_btn(self):
        Checkout_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Checkout']")))
        Checkout_btn.click()
        time.sleep(3)
    
    def EnterOTP_Textfield(self, OTP_guests):
        EnterOTP_Textfield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='otp1']")))
        EnterOTP_Textfield.click()
        EnterOTP_Textfield.send_keys(str(OTP_guests))
        time.sleep(2)

    def Verify_btn(self):
        Verify_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Verify']")))
        Verify_btn.click()
        time.sleep(2)

class UsersCard_Information:
    def __init__(self, driver):
        self.driver = driver

    def switch_to_iframe(self):
        iframe = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^="__privateStripeFrame"]')))
        self.driver.switch_to.frame(iframe)
        time.sleep(5)

    def enter_card_number(self, card_number):
        CardNumbers_Textfield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="number"]')))
        CardNumbers_Textfield.click()
        CardNumbers_Textfield.send_keys(str(card_number))
        time.sleep(2)
    
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def Expiration_Textfield(self, Expiry_Field):
        Expiration_Textfield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="expiry"]')))
        Expiration_Textfield.click()
        Expiration_Textfield.send_keys(str(Expiry_Field))
        time.sleep(2)
    
    def CVC_Textfield(self, CVC_number):
        CVC_Textfield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="cvc"]')))
        CVC_Textfield.click()
        CVC_Textfield.send_keys(str(CVC_number))
        time.sleep(2)

    def PayNow_btn(self):
        PayNow_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='button-text']")))
        PayNow_btn.click()
        time.sleep(2)


class Trackorder:
    def __init__(self, driver):
        self.driver = driver

    def TrackOrder_btn(self):
        TrackOrder_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Track order']")))
        TrackOrder_btn.click() 
        time.sleep(3)
    
#Print orders text
    def Print_OrderNumber(self):
        Print_OrderNumber = self.driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Order Number")]/following-sibling::div[@class="h7 font-semibold"]')
        return Print_OrderNumber.text
    
    def order_type_element(self):
        order_type_element = self.driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Order Type")]/following-sibling::div[@class="h7 font-semibold"]')
        return order_type_element.text  
    
    def guest_element(self):
        guest_element = self.driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Guests")]/following-sibling::div[@class="h7 font-semibold"]')
        return guest_element.text
    
    def Table_No_element(self):
        Table_No_element = self.driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Table No")]/following-sibling::div[@class="h7 font-semibold"]')
        return Table_No_element.text
    
    def Date_type_element(self):
        Date_type_element = self.driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Date")]/following-sibling::div[@class="h7 font-semibold"]')
        return Date_type_element.text

    def Time_type_element(self):
        Time_type_element = self.driver.find_element(By.XPATH, '//div[@class="h7" and contains(text(), "Time")]/following-sibling::div[@class="h7 font-semibold"]')
        return Time_type_element.text

