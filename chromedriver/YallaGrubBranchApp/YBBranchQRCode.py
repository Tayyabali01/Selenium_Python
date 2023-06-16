from xml.dom.minidom import Element
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
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

QRCode_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='fs-9 fw-400 text-black-6 ms-2'][normalize-space()='QR Code']")))
QRCode_Button.click()
time.sleep(2)

AddNewQRCode_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='+ Add New']")))
AddNewQRCode_Button.click()
time.sleep(2)

EnterTableNumber_textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='tableNumber']")))
EnterTableNumber_textfield.click()
EnterTableNumber_textfield.send_keys("643")
time.sleep(2)

Create_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create']")))
Create_Button.click()
time.sleep(2)

OpenNo3_QRCode= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[4]//div[3]//a[1]//*[name()='svg']")))
OpenNo3_QRCode.click()
time.sleep(10)

Back_QRCode= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Back']")))
Back_QRCode.click()
time.sleep(3)

DeleteQRCode_button= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='bg-white bg-opacity-25']//div[4]//div[3]//*[name()='svg']//*[name()='path' and contains(@d,'M432 32H31')]")))
DeleteQRCode_button.click()
time.sleep(2)

ConfirmDeleteQRCode_button= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Delete']")))
ConfirmDeleteQRCode_button.click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)  # Wait for 2 seconds for the scrolling to complete
driver.quit()






