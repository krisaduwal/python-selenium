import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/app/signup.html")

nameElement = driver.find_element(By.XPATH, "//input[@name = 'username']")
nameElement.send_keys('krisaduwal')

emailElement = driver.find_element(By.XPATH, "//input[@name = 'email']")
emailElement.send_keys('hello@g.com')

pwElement = driver.find_element(By.XPATH, "//input[@name = 'password']")
pwElement.send_keys('hello12345')

cpwElement = driver.find_element(By.XPATH, "//input[@name = 'cpassword']")
cpwElement.send_keys('hello12345')

signupElement = driver.find_element(By.XPATH, "//button[@id = 'button1']")

action = ActionChains(driver)
action.click(on_element= signupElement)
action.perform()

time.sleep(20)
# print(element)