from xml.dom.minidom import Element
from selenium import webdriver
import selenium

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

print(selenium.__version__)

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get('http://workcamp-dev.sofit.ltd/')
text_field = driver.find_element_by_class_name("ant-input ant-input-status-error sc-bqWxrE fmSbQs")
text_field.click()


time.sleep(30)




# Find the search box using XPath and send keys
#driver.find_element(by=By.XPATH, value="//input[@id='organization']")