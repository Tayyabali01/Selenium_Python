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

#Click on pending Orders 
PendingOrder_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='Pending']")))
PendingOrder_button.click()
time.sleep(2)



# Click on the first pending order in the dialog box
FirstOrderPending_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstOrderPending_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)


# Find and print the customer details using XPath
ordernumber_element = driver.find_element_by_xpath("//div[@class='modal-body']//div[contains(text(),'Order#')]")
ordernumber = ordernumber_element.text 
expectedtime_element= driver.find_element_by_xpath("//div[@class='modal-body']//div[contains(text(),'Expected Time')]")
expectedtime = expectedtime_element.text
customername_element = driver.find_element_by_xpath("//div[@class='modal-body']//div[@class='fs-8 fw-600 text-gray-3']")
customername= customername_element.text
customerphone_element = driver.find_element_by_xpath("//div[@class='modal-body']//div[@class='fs-7 text-gray-5']")
customerphone= customerphone_element.text

print("Order Number:", ordernumber)
print("Expected Time:", expectedtime)
print("Customer Name:", customername)
print("Customer Phone:", customerphone)
# Get the current time
# #Testing 
# current_time = datetime.datetime.now().time()
# print('hello', current_time)

# Get the current date and time
current_datetime = datetime.datetime.now()

formatted_current_time = current_datetime.strftime("%H:%M on %d %b %Y")

print("Current Date:", formatted_current_time)
# print("Current Month:", current_month)

# # To get automatic date for today
# def get_ordinal_indicator(day):
#     if 11 <= day <= 13:
#         return 'th'
#     else:
#         last_digit = day % 10
#         if last_digit == 1:
#             return 'st'
#         elif last_digit == 2:
#             return 'nd'
#         elif last_digit == 3:
#             return 'rd'
#         else:
#             return 'th'

# Get today's date
# today = datetime.date.today()
# # Get the day of the week and ordinal indicator
# day_of_week = today.strftime("%A")
# day = today.day
# ordinal_indicator = get_ordinal_indicator(day)



# Subtract 1 hour from the current time
# Get target date and time
# target_datetime = datetime(current_datetime.year, current_datetime.month, hour=current_datetime.hour, minute=current_datetime.minute, second=current_datetime.second)

# Extract time from target datetime
# target_time = target_datetime.time()
# target_datetime = datetime.datetime.combine(datetime.date.today(), current_time) - datetime.timedelta(hours=1)
# target_time = target_datetime.time()
# Subtract one hour from the current datetime
# target_time = current_datetime - datetime.timedelta(hours=1)



# Click the first preferred time checkbox
SelectFirstPreferredTime_checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='time1']"))
)
SelectFirstPreferredTime_checkbox.click()

# Get the value of the selected preferred time
selected_preferred_time_element = driver.find_element_by_xpath("//input[@id='time1']/following-sibling::label/div")
selected_preferred_time = selected_preferred_time_element.text

# Print the value of the selected preferred time
print("Selected Preferred Time:", selected_preferred_time)


time.sleep(10)



# print("Target time:", target_time)

# SelectFirstPrefferedtime_checkbox = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.XPATH, "//input[@id='time1']")))
# SelectFirstPrefferedtime_checkbox.click()
# selected_preferred_time_element = driver.find_element_by_xpath("//input[@id='time1']/following-sibling::label/div")
# selected_preferred_time = selected_preferred_time_element.text
# print("Selected Preferred Time:", selected_preferred_time)
# Compare the current time with the target time
if formatted_current_time > selected_preferred_time:

 #Code for canceling the order
    CancelOrder_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel Order']")))
    CancelOrder_btn.click()
    time.sleep(3)
    CancelOrderSuccess_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel and Refund']")))
    CancelOrderSuccess_btn.click()
    print("order cancel successfully", CancelOrderSuccess_btn)
    time.sleep(5)

#Refund screen 
    YesFullRefund_Checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='fullRefund']")))
    YesFullRefund_Checkbox.click()
   
    SelectReason1_Checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='reason1']")))
    SelectReason1_Checkbox.click()
    time.sleep(2)

    Refund_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Refund']")))
    Refund_btn.click()
    time.sleep(5)
    driver.refresh()
else:
#Code for Accepting the order
    SelectFirstPrefferedtime_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='time1']"))
    )
    SelectFirstPrefferedtime_checkbox.click()
    selected_preferred_time_element = driver.find_element_by_xpath("//input[@id='time1']/following-sibling::label/div")
    selected_preferred_time = selected_preferred_time_element.text
    print("Selected Preferred Time:", selected_preferred_time)
    time.sleep(2)

    AcceptOrder_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept Order']"))
    )
    AcceptOrder_btn.click()
    time.sleep(10)

#Click on Running orders
RunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='RunningOrders']")))
RunningOrders_button.click()
time.sleep(2)

# Click on the first pending order in the dialog box
FirstRunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstRunningOrders_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(5)

print("working fine", FirstRunningOrders_button)
time.sleep(8)

order_type_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Order Type')]/following-sibling::div")))
ordertype = order_type_element.text
restaurant_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Restaurant')]/following-sibling::div")))
restaurant= restaurant_element.text
branch_name_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Branch Name')]/following-sibling::div")))
branchname= branch_name_element.text
date_of_order_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Date Of Order')]/following-sibling::div")))
date_of_order= date_of_order_element.text
TimeforPickup_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Time')]/following-sibling::div")))
TimeforPickup= TimeforPickup_element.text
pos_i_element= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'POS I')]/following-sibling::div")))
pos_i= pos_i_element.text 

# Print the extracted information
print("ordertype:" , ordertype)
print("Restaurant:", restaurant)
print("Branch Name:", branchname)
print("Date Of Order:", date_of_order)
print("Table Number:", TimeforPickup)
print("POS I:", pos_i)
time.sleep(2)

SendtoKitchen_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send To Kitchen']")))
SendtoKitchen_button.click()
time.sleep(5)

driver.refresh()
#Click on Running orders
RunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='RunningOrders']")))
RunningOrders_button.click()
time.sleep(2)

# Click on the first pending order in the dialog box
FirstRunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstRunningOrders_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(5)
Readytoserve_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ready to Serve']")))
Readytoserve_button.click()
time.sleep(5)

driver.refresh()
#Click on Running orders
RunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='RunningOrders']")))
RunningOrders_button.click()
time.sleep(2)

# Click on the first pending order in the dialog box
FirstRunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstRunningOrders_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(5)

Serve_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Serve']")))
Serve_button.click()
time.sleep(5)

driver.refresh()
#Click on Running orders
RunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='RunningOrders']")))
RunningOrders_button.click()
time.sleep(2)

# Click on the first pending order in the dialog box
FirstRunningOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstRunningOrders_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(5)

MarkCopleted_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Mark Completed']")))
MarkCopleted_button.click()
time.sleep(5)

driver.refresh()
HistoryOrders_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='History']")))
HistoryOrders_button.click()
time.sleep(2)

# Click on the first pending order in the dialog box
FirstHistoryorder_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='row mx-0 align-items-center'][1]")))
FirstHistoryorder_button.click()
time.sleep(2)

# Scroll within the dialog box to half page 
dialog_box = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg']")
parent_element = dialog_box.find_element(By.XPATH, "./..")  # Locate the parent element of the dialog box

dialog_box_height = dialog_box.size['height']
halfway_point = dialog_box_height // 2

scroll_script = f"arguments[0].scroll(0, {halfway_point})"
driver.execute_script(scroll_script, parent_element)
time.sleep(5)

Close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn btn-outline-pink me-3']")))
Close_button.click()
time.sleep(5)

driver.refresh()
time.sleep(100)
