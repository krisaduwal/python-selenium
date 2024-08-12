import ast
import json
import os
import random
import time
from pathlib import Path

import self
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

env_path = Path('.venv/.env')
load_dotenv(dotenv_path=env_path)

# fetching and converting the string
first_name = ast.literal_eval(os.getenv("FIRSTNAME"))
fElement = random.choice(first_name)
last_name = ast.literal_eval(os.getenv("LASTNAME"))
lElement = random.choice(last_name)


driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")

# def createAccount(driver):
driver.get("https://www.facebook.com/")
time.sleep(5)
# driver.implicitly_wait(10)

createElement = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a")
createElement.click()
time.sleep(2)


fname = driver.find_element(By.XPATH, "//input[@name = 'firstname']")
fname.send_keys(fElement)
time.sleep(1)

lname = driver.find_element(By.XPATH, "//input[@name = 'lastname']")
lname.send_keys(lElement)
time.sleep(1)

myEmail = driver.find_element(By.XPATH, "//input[@name = 'reg_email__']")
myEmail.send_keys(os.getenv("EMAIL"))
time.sleep(1)

reEmail = driver.find_element(By.XPATH, "//input[@name = 'reg_email_confirmation__']")
reEmail.send_keys(os.getenv("EMAIL"))
time.sleep(1)

passWord = driver.find_element(By.XPATH, "//input[@name = 'reg_passwd__']")
passWord.send_keys(os.getenv("PASSWORD"))
time.sleep(2)

dropdown = Select(driver.find_element(By.ID, "month"))
dropdown.select_by_value("12")
time.sleep(1)

dropdown = Select(driver.find_element(By.ID, "day"))
dropdown.select_by_value("8")
time.sleep(1)

dropdown = Select(driver.find_element(By.ID, "year"))
dropdown.select_by_value("2001")
time.sleep(1)

gender = driver.find_element(By.XPATH, "//input[@value = '1']").click()
time.sleep(2)

signUp = driver.find_element(By.XPATH, "//button[@name = 'websubmit']").click()
print("created successfully")
time.sleep(5)
driver.switch_to.window(driver.current_window_handle)


time.sleep(10)

