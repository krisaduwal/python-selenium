# from telnetlib import EC
#explicit waits example

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Foundational Courses"))
)

element.click()
