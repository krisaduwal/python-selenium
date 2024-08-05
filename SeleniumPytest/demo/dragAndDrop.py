#mileko chaina.. k

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")

sourceElement = driver.find_element(By.LINK_TEXT, "Courses")
TargetElement = driver.find_element(By.LINK_TEXT, "Hard")

#action chain object
action = ActionChains(driver)

#drag and drop item
action.drag_and_drop(sourceElement, TargetElement)

action.perform()