import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#webdriver object
driver = webdriver.Chrome()

# #keyword to search
# keyword = "geeks"
# driver.get("https://www.google.co.uk/")
driver.get("http://127.0.0.1:5500/app/signup.html")

#get element
element = driver.find_element(By.XPATH, "//input[@name ='username']")
element.send_keys("krisaa")

#using link text
# element = driver.find_element(By.LINK_TEXT, 'HOME')
# element = driver.find_element(By.PARTIAL_LINK_TEXT, 'HO')

time.sleep(12)
print(element)
