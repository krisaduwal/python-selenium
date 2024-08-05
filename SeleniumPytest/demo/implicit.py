from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://www.geeksforgeeks.org/")
element = driver.find_element(By.LINK_TEXT, "Foundational Courses")
element.click()
