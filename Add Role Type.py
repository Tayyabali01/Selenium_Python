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

Rolematrix_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Role Matrix']")))
Rolematrix_btn.click()

Role_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Roles']")))
Role_btn.click()

AddRoletype_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Add Role Type')]")))
AddRoletype_btn.click()

Roletype_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='title']")))
Roletype_title.click()
Roletype_title.send_keys("HRManager Rabail")

AddPermission_textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-selector']")))
AddPermission_textfield.click()
FirstPermission_textfield = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'PERMISSION_CAMP_CREATE')]")))
FirstPermission_textfield.click()

Modal_Dilaogbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-modal-header']")))
Modal_Dilaogbox.click()

Save_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
Save_btn.click()

AddedRole_firstbtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-eeMvmM gmvdQc']")))
AddedRole_firstbtn.click()

EditDetail_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Edit Details')]")))
EditDetail_btn.click()

Roletype_title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Title']")))
driver.execute_script("arguments[0].value = 'HRManager Rabail'", Roletype_title)

Roletype_Enter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='title']")))
driver.execute_script("arguments[1].value = 'New Text'", Roletype_Enter)

time.sleep(30)