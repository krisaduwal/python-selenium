from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5500/app/signup.html")
# driver.set_page_load_timeout(30)

# current url
# print(driver.current_url)
# print(driver.current_window_handle)

#source code of driver
# print(driver.page_source)

# check if element is visible to user or not
element = driver.find_element(By.ID, 'contact')
print(element.is_displayed())

print(element.get_property('href'))

# gets title
print(driver.title)