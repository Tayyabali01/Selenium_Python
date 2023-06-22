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

class LoginInScreen:
    def __init__(self, driver):
        self.driver = driver 

    def Enter_LoginEmail(self, Enter_Email):
        LoginEmail_textfield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
        LoginEmail_textfield.click()
        LoginEmail_textfield.send_keys(str(Enter_Email))
        time.sleep(2)
    
    def Enter_Password(self, Enter_Password):
        Password_textfield = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        Password_textfield.click()
        Password_textfield.send_keys(str(Enter_Password))
        time.sleep(2)

    def RememberME_Checkbox(self):
        rememberMe_Checkbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='rememberMe']")))
        rememberMe_Checkbox.click()
        time.sleep(2)

    def Login_Button(self):
        Login_Button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        Login_Button.click()
        time.sleep(5)
    
class OrderTracking:
    def __init__(self, driver):
        self.driver = driver
    
    #Click on pending Orders 
    def PendingOrder_button(self):
        PendingOrder_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='Pending']")))
        PendingOrder_button.click()
        time.sleep(2)
    
    # Click on the first pending order in the dialog box
    def FirstOrderPending_button(self):
        FirstOrderPending_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
        FirstOrderPending_button.click()
        time.sleep(2)
        # Scroll within the dialog box to half page 
        dialog_box = self.driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
        parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

        dialog_box_height = dialog_box.size['height']
        halfway_point = dialog_box_height // 2

        scroll_script = f"arguments[0].scroll(0, {halfway_point})"
        self.driver.execute_script(scroll_script, parent_element)

        time.sleep(5)
#Print orders text
    def Printordernumber_element(self):
        ordernumber_element = self.driver.find_element_by_xpath("//div[@class='modal-body']//div[contains(text(),'Order#')]")
        return ordernumber_element.text
    
    def Printexpectedtime_element(self):
        expectedtime_element= self.driver.find_element_by_xpath("//div[@class='modal-body']//div[contains(text(),'Expected Time')]")
        return expectedtime_element.text  
    
    def Printcustomername_element(self):
        customername_element = self.driver.find_element_by_xpath("//div[@class='modal-body']//div[@class='fs-8 fw-600 text-gray-3']")
        return customername_element.text
    
    def Printcustomerphone_element(self):
        customerphone_element = self.driver.find_element_by_xpath("//div[@class='modal-body']//div[@class='fs-7 text-gray-5']")
        return customerphone_element.text
    
    time.sleep(5)

    def SelectFirstPreferredTime_checkbox(self):
        SelectFirstPreferredTime_checkbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='time1']")))
        SelectFirstPreferredTime_checkbox.click()
        time.sleep(2)
    
    def selected_preferred_time_element(self):
        selected_preferred_time_element = self.driver.find_element_by_xpath("//input[@id='time1']/following-sibling::label/div")
        return selected_preferred_time_element.text
    
    def Checkcurrent_time_selected_preferred_time(self, selected_preferred_time):
        current_datetime = datetime.datetime.now()
        formatted_current_time = current_datetime.strftime("%H:%M on %d %b %Y")
        print("Current Date:", formatted_current_time)
        if formatted_current_time > selected_preferred_time:
            # Code for canceling the order
            cancel_order_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel Order']"))
            )
            cancel_order_btn.click()
            time.sleep(3)

            cancel_order_success_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel and Refund']"))
            )
            cancel_order_success_btn.click()
            print("Order canceled successfully", cancel_order_success_btn)
            time.sleep(5)

            # Refund screen
            yes_full_refund_checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='fullRefund']"))
            )
            yes_full_refund_checkbox.click()

            select_reason1_checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='reason1']"))
            )
            select_reason1_checkbox.click()
            time.sleep(2)

            refund_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Refund']"))
            )
            refund_btn.click()
            time.sleep(5)

            self.driver.refresh()
        else:
            # Code for accepting the order
            select_first_preferred_time_checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='time1']"))
            )
            select_first_preferred_time_checkbox.click()

            selected_preferred_time_element = self.driver.find_element_by_xpath("//input[@id='time1']/following-sibling::label/div")
            selected_preferred_time = selected_preferred_time_element.text
            print("Selected Preferred Time:", selected_preferred_time)
            time.sleep(2)

            select_table_dialogbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//select[@id='tableNumbers']"))
            )
            time.sleep(3)

            select = Select(select_table_dialogbox)
            desired_option = "02"  # Replace with the value of the option you want to select
            select.select_by_value(desired_option)

            accept_order_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept Order']"))
            )
            accept_order_btn.click()
            time.sleep(3)
    
    def RunningOrders_button(self):
        RunningOrders_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='RunningOrders']")))
        RunningOrders_button.click()
        time.sleep(5)
    
    def FirstRunningOrders_button(self):
        FirstRunningOrders_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
        FirstRunningOrders_button.click()
        time.sleep(3)

        # Scroll within the dialog box to half page 
        dialog_box = self.driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
        parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box
        dialog_box_height = dialog_box.size['height']
        halfway_point = dialog_box_height // 2

        scroll_script = f"arguments[0].scroll(0, {halfway_point})"
        self.driver.execute_script(scroll_script, parent_element)
        time.sleep(3)
        print("working fine", FirstRunningOrders_button)
        time.sleep(2)
    
    #Print orders text
    def order_type_element(self):
        order_type_element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Order Type')]/following-sibling::div")))
        return order_type_element.text
    
    def restaurant_element(self):
        restaurant_element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Restaurant')]/following-sibling::div")))
        return restaurant_element.text  
    
    def branch_name_element(self):
        branch_name_element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Branch Name')]/following-sibling::div")))
        return branch_name_element.text
    
    def date_of_order_element(self):
        date_of_order_element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Date Of Order')]/following-sibling::div")))
        return date_of_order_element.text
    
    # def time_to_serve_element(self):
    #     time_to_serve_element= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Time to serve')]/following-sibling::div")))
    #     return time_to_serve_element.text
    
    def table_number_element(self):
        table_number_element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Table Number')]/following-sibling::div")))
        return table_number_element.text
   
    def guests_element(self):
        guests_element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Guests')]/following-sibling::div")))
        return guests_element.text
    
    def pos_i_element(self):
        pos_i_element= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'POS I')]/following-sibling::div")))
        return pos_i_element.text
    
    def SendtoKitchen_button(self):
        SendtoKitchen_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send To Kitchen']")))
        SendtoKitchen_button.click()
        time.sleep(50)



    time.sleep(10)
    




# class Create_Reservation:
#     def __init__(self, driver):
#         self.driver = driver