
import time

class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, condition, str_contains):
        element = self.driver.find_element(condition, str_contains)
        return element

    def click_element(self, element):
        element.click()
    
    def send_keys(self, text, element=None):
        element.send_keys(text)
    
    

       
        
