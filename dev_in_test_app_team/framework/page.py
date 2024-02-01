import logging
import time
from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from appium.webdriver.common.appiumby import AppiumBy 
from selenium.webdriver.common.by import By 

from utils.logger import logger

class Page:

    log = logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_appear(self, locator, locator_type="accessibilityid",
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
            by_type = self.get_by_type(locator_type)
            self.log.info('Waiting for element with locator' + locator +' to appear')
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency, 
                                 ignored_exceptions=[
                                     NoSuchElementException,
                                     ElementNotVisibleException,
                                     ElementNotSelectableException,
                                 ])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
        except:
            print_stack()
        return element
    
    def get_by_type(self, locator_type):
        """
        Consume a short-convinient string and returns the By.LOCATORTYPE
        :locator_type: String
        :return: By.LOCATORTYPE
        """
        locator_type = locator_type.lower()
        if locator_type == 'accessibilityid':
            return AppiumBy.ACCESSIBILITY_ID
        elif 'class' in locator_type:
            return By.CLASS_NAME
        elif 'id' in locator_type:
            return By.ID
        elif locator_type == 'xpath':
            return By.XPATH
        elif 'uiautomator' in locator_type:
            return AppiumBy.ANDROID_UIAUTOMATOR
        elif ('link' in locator_type) or ('text' in locator_type):
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator type not supported - or check the argument you passed in")
        return False

    def find_element(self, locator, locator_type='accessibilityid'):
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
            by_type = self.get_by_type(locator_type)
            elements_list = self.driver.find_elements(by_type, locator)
            if len(elements_list) > 0:
                self.log.info("List of elements has been detected in length " + str(len(elements_list)))
            elif len(elements_list) == 1:
                self.log.info("Detected single argumant, find_element would be more suitable for this")
            else:
                self.log.info("Element list is empty. Used locator: '" + locator + "'")
        except:
            self.log.error("Invalid arguments recieved for find_elements_list")
        return elements_list
            
    def click_element(self, locator="", locator_type="accessibilityid", element=None):
        """
        Click action on the element
        """
        try:
            if locator:
                element = self.find_element(locator, locator_type)
            element.click()
            self.log.info('Click performed on element with locator' + locator)
        except:
            self.log.error(
                "Can't permorm click on element with locator" + locator
            )
            print_stack()
        
    def send_info(self, info, locator="", locator_type="accessibilityid", element=None):
        """
        Send keys to input field
        """
        try:
            if locator:
                element = self.find_element(locator, locator_type)
            element.send_keys(info)
            self.log.info('Information was sent to element with locator '+locator)
        except:
            self.log.error(
                "Failed to send information to element with locator "+locator
            )
            print_stack()
    
    def get_text(self, element=None, info=""): 
        """
        Get Text from the element
        """
        try:
            text = element.text
            if len(text) > 0:
                self.log.info("Text of the element "+ info +"is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Unable to get text of the element" + info)
            text = None
        return text
    
    def clear_field(self, locator="", locator_type="accessibilityid", element=None):
        """
        Clear field of provided element or just use combination of locator and locator_type
        to not repeat yourself
        """
        
        if locator:
            self.log.debug("clearing field of element by locator")
            element = self.find_element(locator, locator_type)
        element.clear()
        self.log.info("Element has been cleared maybe with provided locator"+ locator)
    
    def is_element_present(self, locator="", locator_type="accessibilityid", element=None):
        """
        Check for presence of an element 
        return boolean value 
        """
        try:
            if locator:
                element = self.find_element(locator, locator_type)
            if element is not None:
                self.log.info("Element with locator" + "is presented")
                return True
            else:
                return False
        except:
            self.log.error("No element with locator" + locator +"presented")
        return False
    
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
    
    def is_element_displayed(self, locator="", locator_type="accessibilityid", element=None):
        """
        Mock of is_displayed() webdriver method
        """
        is_displayed = False
        try:
            if locator:
                element = self.find_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator" + locator)
            else:
                self.log.info("Element is not displayed with locator" + locator)
                return is_displayed
        except:
            self.log.error("Error on 'is_element_displayed'")
        return is_displayed
    
    def is_element_enabled(self, locator="", locator_type="accessibilityid", element=None):
        """
        Checking whether the specified element is enabled or not
        """
        is_enable = False
        try:
            if locator:
                element = self.find_element(locator, locator_type)
            is_enable = element.is_enabled()
            if is_enable:
                self.log.info("Element is enable")
            else:
                self.log.info("Element is disabled") 
        except:
            self.log.error("Element state couldn't be determined")
        return is_enable
    





       
            
            
    
    

       
        
