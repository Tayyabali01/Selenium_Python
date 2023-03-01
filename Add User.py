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

Join_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-hLBbgP jbaWzw']")))
Join_btn .click()

Email_Text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
Email_Text.click()
Email_Text.send_keys("tayyab2@mailinator.com")

Password_Text= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
Password_Text.click()
Password_Text.send_keys("Ali12345")

Rememberme_checkbox= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Remember me']")))
Rememberme_checkbox.click()

Signin_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Signin_btn .click()


#self method 
text_msg=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Users']/self::a"))).text
print(text_msg)

User_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Users']")))
User_btn .click()

AddUser_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Add user')]")))
AddUser_btn .click()

AddUserName_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fullName']")))
AddUserName_btn .click()
AddUserName_btn.send_keys("Asad")

AddUserEmail_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
AddUserEmail_btn .click()
AddUserEmail_btn.send_keys("Asad1@mailinator.com")

AddUserRole_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-selector']")))
AddUserRole_btn .click()
SelectUser_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='User']")))
SelectUser_btn.click()

Proceed_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Proceed_btn.click()

time.sleep(10)

AddUser_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Add user')]")))
AddUser_btn .click()

AddUserName_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fullName']")))
AddUserName_btn .click()
AddUserName_btn.send_keys("Awais")

AddUserEmail_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
AddUserEmail_btn .click()
AddUserEmail_btn.send_keys("Awais@mailinator.com")

AddUserRole_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-selector']")))
AddUserRole_btn .click()
SelectUser_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='User']")))
SelectUser_btn.click()

Proceed_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Proceed_btn.click()

time.sleep(10)

AddUser_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Add user')]")))
AddUser_btn .click()

AddUserName_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fullName']")))
AddUserName_btn .click()
AddUserName_btn.send_keys("Muneeb")

AddUserEmail_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
AddUserEmail_btn .click()
AddUserEmail_btn.send_keys("Muneeb1@mailinator.com")

AddUserRole_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-selector']")))
AddUserRole_btn .click()
SelectUser_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='User']")))
SelectUser_btn.click()

Proceed_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Proceed_btn.click()

time.sleep(10)

AddUser_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Add user')]")))
AddUser_btn .click()

AddUserName_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fullName']")))
AddUserName_btn .click()
AddUserName_btn.send_keys("Sunaira")

AddUserEmail_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
AddUserEmail_btn .click()
AddUserEmail_btn.send_keys("Sunaira@mailinator.com")

AddUserRole_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-selector']")))
AddUserRole_btn .click()
SelectUser_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='User']")))
SelectUser_btn.click()

Proceed_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Proceed_btn.click()

time.sleep(50)
#comment