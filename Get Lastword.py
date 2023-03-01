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

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get('http://workcamp-dev.sofit.ltd/')
get_security_question= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-hLBbgP jbaWzw']")))
sentence = get_security_question.text
last_word =sentence.rsplit()[-1]
last_word= last_word[:-1]
answer=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-hLBbgP jbaWzw']")))
answer.send_keys(last_word)
