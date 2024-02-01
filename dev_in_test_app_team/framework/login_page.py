from .page import Page


class LoginPage(Page):
    
    _hello_login_btn_xpath = '//android.widget.FrameLayout[@resource-id="com.ajaxsystems:id/authHelloLogin"]'
    #Authorization Login page elements path
    _email_login_field_xpath = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'
    _passw_login_field_xpath  = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'
    _auth_login_btn_xpath = '//android.widget.FrameLayout[@resource-id="com.ajaxsystems:id/authLogin"]'
    #Decided to put tit here and make less noise in tests
    #Realize this is not part of login page, but count it as a way to go back to perform login
    _menu_bar_app_xpath = '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
    _app_settings_xpath = '//android.view.View[@resource-id="com.ajaxsystems:id/settings"]'
    _sign_out_btn_xpath = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Sign Out"]'
  

    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def assert_hello_login_btn_exists(self):
        return self.is_element_present(locator=self._hello_login_btn_xpath, locator_type='xpath')
    
    def navigate_to_input_login_page(self):
        self.click_element(locator=self._hello_login_btn_xpath, locator_type='xpath')
    
    def assert_hello_login_navigation_correctness(self):
        forgot_passw = self.find_element(locator=
                                         '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Forgot password?"]',
                                         locator_type='xpath')
        
        return self.is_element_displayed(element=forgot_passw)
    
    def input_email_password(self, email="", password=""):
        if email:
             self.send_info(locator=self._email_login_field_xpath, locator_type='xpath' , info=email)
        if password:
            self.send_info(locator=self._passw_login_field_xpath, locator_type='xpath', info=password) 
    
    def click_login_auth_submit(self):
        self.click_element(locator=self._auth_login_btn_xpath, locator_type='xpath')
        self.driver.implicitly_wait(3)

    def email_login_field_clear(self):
        self.clear_field(locator=self._email_login_field_xpath, locator_type='xpath')
    
    def passw_login_field_clear(self):
        self.clear_field(locator=self._passw_login_field_xpath, locator_type='xpath')

    def sign_out_and_navigate_to_login(self):
        self.click_element(locator=self._menu_bar_app_xpath, locator_type='xpath')
        self.click_element(locator=self._app_settings_xpath, locator_type='xpath')
        self.click_element(locator=self._sign_out_btn_xpath, locator_type='xpath')
        self.navigate_to_input_login_page()
        self.email_login_field_clear()
        self.passw_login_field_clear()


