from appium.webdriver.common.appiumby import AppiumBy
import time

class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, str_contains: str):
        self.element = self.driver.find_element(AppiumBy.CLASS_NAME, str_contains)
        return self.element

    def click_element(self):
        self.element.click()
        time.sleep(2)
