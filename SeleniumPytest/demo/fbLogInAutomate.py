import time

from dotenv import load_dotenv, dotenv_values

import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# manually load .env file path
env_path = Path('../.venv/.env')
load_dotenv(dotenv_path=env_path)

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

emailElement = driver.find_element(By.ID, 'email')
emailElement.send_keys(os.getenv("MY_EMAIL"))

pwElement = driver.find_element(By.ID, 'pass')
pwElement.send_keys(os.getenv("MY_PASS"))

loginElement = driver.find_element(By.NAME, "login")

action = ActionChains(driver)
action.click(on_element= loginElement)
action.perform()

# print(emailElement)
# my_key = os.getenv("MY_KEY")
# print(my_key)
time.sleep(10)