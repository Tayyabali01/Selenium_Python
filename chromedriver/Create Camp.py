from xml.dom.minidom import Element
from selenium import webdriver
import selenium

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
import time

print(selenium.__version__)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get('http://workcamp-dev.sofit.ltd/')
Camp_Name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='organization']")))
# click the element
Camp_Name.click()
# enter text
Camp_Name.send_keys("TayyabShadab")


Proceed_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Proceed_btn .click()
#Proceed_btn.click()

Originazation_Name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='orgName']")))
Originazation_Name .click()
Originazation_Name.send_keys("Sofit")

Team_strength = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-selector']")))
Team_strength .click()

Team_Strength_2ndItem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='11-50']")))
Team_Strength_2ndItem .click()

Proceed_submitbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Proceed_submitbtn .click()

Signup_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
Signup_email.click()
Signup_email.send_keys("tayyab2@mailinator.com")

Signup_Name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fullName']")))
Signup_Name.click()
Signup_Name.send_keys("Tayyab Ali")

Signup_Password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
Signup_Password.click()
Signup_Password.send_keys("Ali12345")
#Show_Password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='eye']//*[name()='svg']")))

Signup_ConfPassword = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='confirmPassword']")))
Signup_ConfPassword.click()
Signup_ConfPassword.send_keys("Ali12345")
#Show_ConfPassword = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='eye-invisible']//*[name()='svg']")))

Proceed_Signupcomp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Proceed_Signupcomp .click()



time.sleep(500)




# Find the search box using XPath and send keys
#driver.find_element(by=By.XPATH, value="//input[@id='organization']")