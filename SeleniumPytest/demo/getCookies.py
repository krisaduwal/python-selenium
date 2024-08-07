import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")

print(driver.get_cookies())

# gets x and y position of window
print(driver.get_window_position(windowHandle= 'current'))

# gets x, y and height and width
print(driver.get_window_rect())

# set wait time
driver.implicitly_wait(30)

# print(driver.get_screenshot_as_base64())

# take screenshot from driver
# print(driver.get_screenshot_as_file("poo.png"))
# print(driver.get_screenshot_as_png())

# get browser log
# driver.get_log("browser")
# time.sleep(20)