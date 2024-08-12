import time
import os
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

dotenv_path = Path('.venv/.env')
load_dotenv(dotenv_path=dotenv_path)

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=options)

driver.get("https://www.daraz.com.np/")
time.sleep(2)

login = driver.find_element(By.LINK_TEXT, "LOGIN")
login.click()

driver.switch_to.window(driver.current_window_handle)
time.sleep(2)

userId = driver.find_element(By.XPATH, "//*[@type='text']")
userId.send_keys(os.getenv("NUM"))
time.sleep(1)

user_password = driver.find_element(By.XPATH, "//*[@type='password']")
user_password.send_keys(os.getenv("PASS"))
time.sleep(2)

driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
print("login successful")
driver.switch_to.window(driver.current_window_handle)
time.sleep(50)

# text = driver.find_element(By.XPATH, "//li[@id = 'My-profile']").text
# assert "My Profile" in text
# print("passed")

# time.sleep(20)