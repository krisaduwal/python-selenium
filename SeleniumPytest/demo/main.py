import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://127.0.0.1:5500/app/signup.html")
# driver.get("https://www.google.com/")
# driver.quit()
element = driver.find_element(By.ID, "username")
# element = driver.find_element(By.NAME, "q")
element.send_keys("krisaduwal")
mail = driver.find_element(By.ID, "email")
mail.send_keys("holo", Keys.ENTER)
time.sleep(120)