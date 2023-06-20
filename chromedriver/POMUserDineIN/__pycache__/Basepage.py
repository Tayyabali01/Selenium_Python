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
from locators import UserApp_SelectItem
from locators import Create_Reservation
from locators import Personal_Information
from locators import UsersCard_Information
from locators import Trackorder
from Testdata import Testdata

chrome_driver_path = ChromeDriverManager().install()
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(Testdata.User_Url)
driver.maximize_window()
#Select Item and Add to Cart Successfully
User= UserApp_SelectItem(driver)
User.WAKHA_AlBrasha()
User.Breadsitem_btn()
User.BlackseedNaan_item()
User.Select1_btn()
User.Addtocart_btn()
User.AddTip_btn()
User.LetsPlanYourOrder_btn()

# User Reservation Screen
user_reservation = Create_Reservation(driver)
user_reservation.enter_no_of_guests(10)
user_reservation.SelectDate_textbox()
user_reservation.SelectPrefferedtime_textbox()
user_reservation.Select2ndTimeSlot_textbox()
user_reservation.Select3rdTimeSlot_textbox()
user_reservation.Next_btn()

#User Personal Information
Enter_Information = Personal_Information(driver) 
Enter_Information.FullName_Textfield('Page Object Model Automation Testing')
Enter_Information.Email_Textfield('tayyabalishansa123@gmail.com')
Enter_Information.PhoneNumber_Textfield(1527773703)
Enter_Information.Checkout_btn()
Enter_Information.EnterOTP_Textfield(55690)
Enter_Information.Verify_btn()

#UsersCard Information
Card_Information = UsersCard_Information(driver)
Card_Information.switch_to_iframe()
Card_Information.enter_card_number("4242 4242 4242 4242")
Card_Information.switch_to_default_content()
Card_Information.switch_to_iframe()
Card_Information.Expiration_Textfield("1256")
Card_Information.switch_to_default_content()
Card_Information.switch_to_iframe()
Card_Information.CVC_Textfield("776")
Card_Information.switch_to_default_content()
Card_Information.PayNow_btn()

#TrackOrder Screen
TrackingOrderInformation = Trackorder(driver)
TrackingOrderInformation.TrackOrder_btn()

# UserReservation= Create_Reservation(driver)
# UserReservation.NoOfGuests_textbox()



