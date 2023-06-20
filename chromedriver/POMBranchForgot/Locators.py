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

class ForgotPassword:
    def __init__(self, driver):
        self.driver = driver
    
    def Forgot_Password(self):
        ForgotPassword_btn= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text-pink']")))
        ForgotPassword_btn.click()
        time.sleep(2)

    def EnterEmail_Textfiled(self, email_textfield):
        no_of_guests_textbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
        no_of_guests_textbox .click()
        no_of_guests_textbox .send_keys(str(email_textfield))
        time.sleep(2)

    def ResetPassword_Button(self):
        ResetPassword_Button= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        ResetPassword_Button.click()
        time.sleep(3)

    def Close_Button(self):
        Close_Button= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Close']")))
        Close_Button.click()
        time.sleep(15)

         