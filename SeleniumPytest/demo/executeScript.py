import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/app/signup.html")
driver.fullscreen_window()

# write script
script = "alert('alert via selenium')"

# generate alert via js using async
# driver.execute_async_script(script)
driver.execute_script(script)
time.sleep(10)