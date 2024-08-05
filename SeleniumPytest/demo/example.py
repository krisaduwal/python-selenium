import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Example(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSearch(self):

        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)

        element = driver.find_element(By.NAME, "q")
        element.send_keys("pycache")
        element.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        # time.sleep(60)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

