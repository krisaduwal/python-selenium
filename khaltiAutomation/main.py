import os
import time
from _ast import Assert
from pathlib import Path

import dotenv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

env_path = Path('.venv/.env')
load_dotenv(dotenv_path=env_path)

driver = webdriver.Chrome()


driver.get("https://web.khalti.com/?csrt=9371343960400989664#/")



phoneElement = driver.find_element(By.XPATH, "//input[@name = 'id']")
phoneElement.send_keys(os.getenv("MY_NUM"))

passElement = driver.find_element(By.XPATH, "//input[@name = 'password']")
passElement.send_keys(os.getenv("MY_PASS"))

loginElement = driver.find_element(By.XPATH, "//button[@role = 'button']")
loginElement.click()
time.sleep(30)
# action = ActionChains(driver)
# action.click(on_element=loginElement)
# action.perform()

driver.switch_to.window(driver.current_window_handle)
print(driver.current_url)
time.sleep(10)


transferElement = driver.find_element(By.XPATH, "//div[@class='fundText--1pdtF' and text() = 'Transfer']")
transferElement.click()

driver.switch_to.window(driver.current_window_handle)
print(driver.current_url)

inputNum = driver.find_element(By.XPATH, "//input[@name='user']")
inputNum.send_keys("9861550096")

amountElement = driver.find_element(By.XPATH, "//input[@name = 'amount']")
amountElement.send_keys("10")

# purposeElement = driver.find_element(By.XPATH, "//div[@role = 'listbox']")
# purposeElement.click()

submitElement = driver.find_element(By.XPATH, "//button[@class = 'ui primary button']")
submitElement.click()

print(driver.current_url)

driver.implicitly_wait(50)
element = driver.find_element(By.XPATH, "//div[@class = 'ui primary button' and text() = 'Ok']")
element.click()

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//div[@class = 'ui primary button' text() = 'Ok']"))
#     )
#     element.click()
# finally:
#     driver.quit()
# for
# driver.switch_to.window()
# print(driver.current_url)

# okElement = driver.find_element(By.XPATH, "//div[@class = 'ui primary button' and text() = 'Ok']")
# okElement.click()
# expectedURL = driver.current_url
# actualURL = "https://web.khalti.com/#/"

# Assert.assertEquals(actualURL, expectedURL)

# action.reset_actions()


# driver.get("https://web.khalti.com/#/")
# fundElement = driver.find_element(By.CLASS_NAME, "FundItem--1yG4v")

# action.click(on_element= fundElement)
# action.perform()
time.sleep(100)