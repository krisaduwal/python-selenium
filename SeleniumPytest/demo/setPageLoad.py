from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.geeksforgeeks.org/")
# driver.set_page_load_timeout(30)

# current url
print(driver.current_url)
print(driver.current_window_handle)