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
from selenium.webdriver.chrome.service import Service
from locators import LoginInScreen
from locators import OrderTracking
from Testdata import testdata


chrome_driver_path = ChromeDriverManager().install()
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(testdata.User_Url)
driver.maximize_window()
#Select Item and Add to Cart Successfully
LoginScreen= LoginInScreen(driver)
LoginScreen.Enter_LoginEmail('wakha_albarsha@gmail.com')
LoginScreen.Enter_Password('12341234')
LoginScreen.RememberME_Checkbox()
LoginScreen.Login_Button()

Ordersection=OrderTracking(driver)
Ordersection.PendingOrder_button()
Ordersection.FirstOrderPending_button()
text=Ordersection.Printordernumber_element()
print(text)
text1=Ordersection.Printexpectedtime_element()
print(text1)
text2=Ordersection.Printcustomername_element()
print(text2)
text3=Ordersection.Printcustomerphone_element()
print(text3)
Ordersection.SelectFirstPreferredTime_checkbox()
text4=Ordersection.selected_preferred_time_element()
print(text4)
Ordersection.Checkcurrent_time_selected_preferred_time('selected_preferred_time')
Ordersection.RunningOrders_button()
Ordersection.FirstRunningOrders_button()
text5=Ordersection.order_type_element()
print(text5)
text6=Ordersection.restaurant_element()
print(text6)
text7=Ordersection.branch_name_element()
print(text7)
text8=Ordersection.date_of_order_element()
print(text8)
text10=Ordersection.table_number_element()
print(text10)
text11=Ordersection.guests_element()
print(text11)
text12=Ordersection.pos_i_element()
print(text12)
Ordersection.SendtoKitchen_button()
