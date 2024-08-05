import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("http://127.0.0.1:5500/app/signup.html")
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
element = driver.find_element(By.LINK_TEXT, "Foundational Courses")
anotherElement = driver.find_element(By.LINK_TEXT, "Data Science")
# element = driver.find_element(By.LINK_TEXT, "SKILLS")

#create action chain object
action = ActionChains(driver)

#keydown
#action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()

#clicks the item
action.click(on_element = element)
action.reset_actions()
action.click(on_element= anotherElement)

#release the item
# action.release(on_element= element)

#moves the cursor
# action.move_by_offset(200, 200)

#move to element
# action.move_to_element(element).click().perform()


#perform
action.perform()
# time.sleep(16)