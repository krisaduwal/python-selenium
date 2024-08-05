import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/app/signup.html")
element = driver.find_element(By.LINK_TEXT, "LOG IN")

#create action chain object
action = ActionChains(driver)

#clicks the item
action.context_click(on_element = element)

#perform
action.perform()
time.sleep(16)