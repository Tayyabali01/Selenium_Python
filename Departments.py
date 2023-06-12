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
from selenium.webdriver.common.keys import Keys
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

#Department_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Departments']")))
#Department_btn.click()

#Add_Department_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Add Department')]")))
#Add_Department_btn.click()
#Enter_Department_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']")))
#Enter_Department_btn.click()
#Enter_Department_btn.send_keys("AI Team")
#Proceed_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Proceed']")))
#Proceed_btn.click()

User_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Users']")))
User_btn .click()
AlreadyaddedAsad_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//td[normalize-space()='Asad']")))
AlreadyaddedAsad_btn.click()
#Recenedinvite_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Resend Invite')]")))
#Recenedinvite_btn.click()
#Close_Dilogbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-kMjNwy jiepcs']//span[@aria-label='close']//*[name()='svg']//*[name()='path' and contains(@d,'M563.8 512')]")))
#Close_Dilogbox.click()

Editdetails_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Edit Details')]")))
Editdetails_btn.click()
Fullname_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Full Name']")))
Fullname_btn.click()



Phonenumber_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Phone Number']")))
Phonenumber_btn.click()
Phonenumber_btn.send_keys("+923160882802")

Role_Dilaogbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@title='User']")))
Role_Dilaogbox.click()
SelectUser_Dilaogbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='User']")))
SelectUser_Dilaogbox.click()




Department_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@title='General']")))
Department_btn.click()

time.sleep(30)
