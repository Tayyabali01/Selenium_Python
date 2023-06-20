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
from Locators import ForgotPassword

from Testdata import Testdata

chrome_driver_path = ChromeDriverManager().install()
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(Testdata.User_Url)
driver.maximize_window()
#Select Item and Add to Cart Successfully
User= ForgotPassword(driver)
User.Forgot_Password()
User.EnterEmail_Textfiled("tayyabalisa123@gmail.com")
User.ResetPassword_Button()
User.Close_Button()