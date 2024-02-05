import logging
import time
from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (NoSuchElementException,
                                     ElementNotVisibleException,
                                     ElementNotSelectableException)


from utils.logger import logger

class Page:

    log = logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_appear(self, locator, locator_type,
                                  timeout=10, pollFrequency=0.3):
        """
        Waits for an element on expected condition to be clickable
        : locator: str / Ex: 'id_name'
        : locatorType: provided by get_bytype on simple str / Ex: 'accessibilityid'
        : timeout: int in seconds, timeout length
        : pollFrequency: polling interval for frequent code evaluation
        """
        element = None # None servers sentinel role 
        try:
            self.log.info('Waiting for element with locator' + locator +' to appear')
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency, 
                                 ignored_exceptions=[
                                     NoSuchElementException,
                                     ElementNotVisibleException,
                                     ElementNotSelectableException,
                                 ])
            element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        except:
            print_stack()
        return element
    

    def find_element(self, locator, locator_type):
        """
        Search for an element on a page 
        """
        element = None
        try:
            element = self.wait_until_element_appear(locator=locator, 
                                                     locator_type=locator_type)
            if element is not None:
                self.log.info("Element found with locator: '" + locator + "'")
            else:
                self.log.info('Search for element has not been successful, locator: '+locator)
        except:
            self.log.error("Element hasn\'t been found with locator: '" + locator + "'")
        return element

    def find_elements_list(self, locator, locator_type):
        """
        Gather inquired list of elements
        """
        elements_list = None
        try:
            elements_list = self.driver.find_elements(locator_type, locator)
            if len(elements_list) > 0:
                self.log.info("List of elements has been detected in length " + str(len(elements_list)))
            elif len(elements_list) == 1:
                self.log.info("Detected single argumant, find_element would be more suitable for this")
            else:
                self.log.info("Element list is empty. Used locator: '" + locator + "'")
        except:
            self.log.error("Invalid arguments recieved for find_elements_list")
        return elements_list
            
    def click_element(self, element=None):
        """
        Click action on the element
        """
        try:
            element.click()
            self.log.info('Click performed on element with locator' + repr(element))
        except:
            self.log.error(
                "Can't permorm click on element" + repr(element)
            )
            print_stack()
        
    def send_info(self, text, element=None):
        """
        Send keys to input field
        """
        try:
            element.send_keys(text)
            self.log.info('Information: '+text+' was sent to element '+ repr(element))
        except:
            self.log.error(
                "Failed to send information "+text+" to element "+ repr(element)
            )
            print_stack()
    
    def get_text(self, element=None): 
        """
        Get Text from the element
        """
        try:
            text = element.text
            if len(text) > 0:
                self.log.info("Text of the element is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Unable to get text of the element")
            text = None
        return text
    
    def clear_field(self, element=None):
        """
        Clear field of provided element or just use combination of locator and locator_type
        to not repeat yourself
        """
        element.clear()
        self.log.info("Element "+repr(element)+" has been cleared")
    
    
    def list_element_presence(self, locator, locator_type="accessibilityid"):
        """
        Elements detector 
        return bolean  True/False
        """
        try:
            elements_list = self.find_elements_list(locator, locator_type)
            if len(elements_list) > 0:
                self.log.info("Number of elements found:" + str(len(elements_list)))
                return True
            return False
        except:
            self.log.error("Element(s) are not presented")
            return False
    
    def is_element_displayed(self, element=None):
        """
        Mock of is_displayed() webdriver method
        """
        is_displayed = False
        try:
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element is not displayed ")
                return is_displayed
        except:
            self.log.error("Error on 'is_element_displayed'")
        return is_displayed
    
    def is_element_enabled(self, element=None):
        """
        Checking whether the specified element is enabled or not
        """
        is_enable = False
        try:
            is_enable = element.is_enabled()
            if is_enable:
                self.log.info("Element is enable")
            else:
                self.log.info("Element is disabled") 
        except:
            self.log.error("Element state couldn't be determined")
        return is_enable
    





       
            
            
    
    

       
        
