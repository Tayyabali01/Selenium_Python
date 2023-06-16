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

Menu_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='fs-9 fw-400 text-black-6 ms-2'][normalize-space()='Menu']")))
Menu_Button.click()
time.sleep(2)

DessertFirstItem_InstockSwitch = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/label[1]")))
DessertFirstItem_InstockSwitch.click()
time.sleep(3)

DessertFirstItem_DineInSwitch = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='container0']//div[@class='row gap-2']//div[1]//div[1]//div[1]//div[1]//div[2]//div[2]//div[3]//div[1]//label[1]")))
DessertFirstItem_DineInSwitch.click()
time.sleep(3)

DessertFirstItem_PickUpSwitch = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='container0']//div[@class='row gap-2']//div[1]//div[1]//div[1]//div[1]//div[2]//div[2]//div[3]//div[2]//label[1]")))
DessertFirstItem_PickUpSwitch.click()
time.sleep(3)

DessertFirstItem_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")))
DessertFirstItem_click .click()
time.sleep(3)

DessertFirstItem_closebutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Close']")))
DessertFirstItem_closebutton .click()
time.sleep(3)

DessertMinimize_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div/div[@class='bg-white bg-opacity-25']/div[@class='row m-0']/div[@class='col-md-10 bg-light pt-4 pb-4 min-vh-100']/div[@class='container-fluid']/div[2]/div[1]/div[2]/span[1]//*[name()='svg']")))
DessertMinimize_btn .click()
time.sleep(3)

DessertMinimize_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div/div[@class='bg-white bg-opacity-25']/div[@class='row m-0']/div[@class='col-md-10 bg-light pt-4 pb-4 min-vh-100']/div[@class='container-fluid']/div[2]/div[1]/div[2]/span[1]//*[name()='svg']")))
DessertMinimize_btn .click()
time.sleep(3)

DessertMaximize_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ms-auto collapsed']//span[@class='arrow-icon']//*[name()='svg']//*[name()='path' and contains(@d,'M504 256c0')]")))
DessertMaximize_btn .click()
time.sleep(3)


Save_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
Save_btn.click()
print("Changes save successfully:" , Save_btn)
time.sleep(3)


