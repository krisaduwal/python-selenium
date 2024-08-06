import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DragTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_drag_drop(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://jqueryui.com/draggable/')
        driver.switch_to.frame(0)

        # find source element
        sourceElement = driver.find_element(By.ID, 'draggable')


        action = ActionChains(driver)
        action.drag_and_drop_by_offset(sourceElement, 100, 100)
        action.perform()

        time.sleep(5)

        driver.get('https://jqueryui.com/droppable/')
        driver.switch_to.frame(0)

        sourceElement = driver.find_element(By.ID, 'draggable')
        targetElement = driver.find_element(By.ID, 'droppable')

        action2 = ActionChains(driver)
        action2.drag_and_drop(sourceElement, targetElement).perform()
        time.sleep(6)

        self.assertEqual('Dropped!', targetElement.text)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

