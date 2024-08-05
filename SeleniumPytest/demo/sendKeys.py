import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/app/signup.html")

# adding cookies
driver.add_cookie({"name": "poo", "value": "oop"})

# find element by xpath and send keys
nameElement = driver.find_element(By.XPATH, "//input[@name = 'username']")
nameElement.send_keys('krisaduwal')

emailElement = driver.find_element(By.XPATH, "//input[@name = 'email']")
# emailElement.send_keys('hello@g.com')

# creating web element , acts as a clone element
id = emailElement._id
emailElement_clone = driver.create_web_element(id)
emailElement_clone.send_keys('hello@b.com')


pwElement = driver.find_element(By.XPATH, "//input[@name = 'password']")
pwElement.send_keys('hello12345')

cpwElement = driver.find_element(By.XPATH, "//input[@name = 'cpassword']")
cpwElement.send_keys('hello12345')

signupElement = driver.find_element(By.XPATH, "//button[@id = 'button1']")

action = ActionChains(driver)
action.click(on_element= signupElement)
action.perform()

time.sleep(10)
# print(element)