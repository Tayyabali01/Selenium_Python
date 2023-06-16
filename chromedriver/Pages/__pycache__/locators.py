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

class UserApp:
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
        time.sleep(50)