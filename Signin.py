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
Camp_Name.send_keys("Usman")

Join_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-hLBbgP jbaWzw']")))
Join_btn .click()

Email_Text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
Email_Text.click()
Email_Text.send_keys("tayyab2@mailinator.com")

Password_Text= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
Password_Text.click()
Password_Text.send_keys("Testing12")

Rememberme_checkbox= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Remember me']")))
Rememberme_checkbox.click()

Signin_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Signin_btn .click()


#self method 
text_msg=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Users']/self::a"))).text
print(text_msg)



time.sleep(30)

"""#Again sigup if not sigin successfully
Signup_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign Up']")))
Signup_btn .click()

Signup_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
Signup_email.click()
Signup_email.send_keys("tayyabalisa123@gmail.com")

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

"""
