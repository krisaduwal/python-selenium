from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.get("https://www.geeksforgeeks.org/data-structures/")
driver.get("https://www.geeksforgeeks.org/system-design-tutorial/")

# one step back in browser
driver.back()