from .page import Page

from appium.webdriver.common.appiumby import AppiumBy 
from selenium.webdriver.common.by import By 

class LoginPage(Page):
    
    _hello_login_btn_xpath = '//android.widget.FrameLayout[@resource-id="com.ajaxsystems:id/authHelloLogin"]'
    #Authorization Login page elements path
    _email_login_field_xpath = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'
    _passw_login_field_xpath  = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'
    _auth_login_btn_xpath = '//android.widget.FrameLayout[@resource-id="com.ajaxsystems:id/authLogin"]'
    #Decided to put tit here and make less noise in tests
    _forgot_pass_text_xpath = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Forgot password?"]'
    

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def assert_hello_login_btn_exists(self):
        hello_login_btn = self.find_element(locator=self._hello_login_btn_xpath, locator_type=By.XPATH)
        return self.is_element_displayed(hello_login_btn)
    
    def navigate_to_input_login_page(self):
        hello_login_btn = self.find_element(locator=self._hello_login_btn_xpath, locator_type=By.XPATH)
        self.click_element(hello_login_btn)
    
    def assert_hello_login_navigation_correctness(self):
        forgot_passw_text = self.find_element(locator= self._forgot_pass_text_xpath,
                                         locator_type=By.XPATH)
        
        return self.is_element_displayed(element=forgot_passw_text)
    
    def click_login_auth_submit(self):
        login_auth_btn = self.find_element(locator=self._auth_login_btn_xpath, 
                                           locator_type=By.XPATH)
        self.click_element(login_auth_btn)
        self.driver.implicitly_wait(3)

    def get_email_login_field(self):
        return self.find_element(locator=self._email_login_field_xpath, 
                                 locator_type=By.XPATH)
    
    def get_password_login_field(self):
        return self.find_element(locator=self._passw_login_field_xpath, 
                                 locator_type=By.XPATH)

    


