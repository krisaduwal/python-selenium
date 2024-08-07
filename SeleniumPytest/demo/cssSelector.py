import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("http://127.0.0.1:5500/app/signup.html")
driver.fullscreen_window()


element = driver.find_element(By.CSS_SELECTOR, ".nav ")
print(element)
time.sleep(5)