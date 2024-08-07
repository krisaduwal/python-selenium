import os
import time
from _ast import Assert
from pathlib import Path

import dotenv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

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


# driver.forward()
# driver.get("https://web.khalti.com/#/")
transferElement = driver.find_element(By.XPATH, "//*[@class='FundItem--1yG4v']")
# transferElement = driver.find_element(By.LINK_TEXT, "Transfer")
transferElement.click()
# expectedURL = driver.current_url
# actualURL = "https://web.khalti.com/#/"

# Assert.assertEquals(actualURL, expectedURL)

# action.reset_actions()


# driver.get("https://web.khalti.com/#/")
# fundElement = driver.find_element(By.CLASS_NAME, "FundItem--1yG4v")

# action.click(on_element= fundElement)
# action.perform()
time.sleep(100)