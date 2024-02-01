from .login_page import LoginPage

class HomeHubPage(LoginPage):
    _add_new_hub_btn_xpath = '//android.view.ViewGroup[@resource-id="com.ajaxsystems:id/hubAdd"]'
    _menu_bar_app_xpath = '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
    _app_settings_xpath = '//android.view.View[@resource-id="com.ajaxsystems:id/settings"]'
    _sign_out_btn_xpath = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Sign Out"]'
  

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def add_new_hub(self):
        self.click_element(locator=self.add_new_hub, locator_type='xpath')
    
    def assert_add_hub_button(self):
        return (self.is_element_present(locator=self._add_new_hub_btn_xpath, locator_type='xpath'))
    
    def click_side_menu_bar(self):
        self.click_element(locator=self._menu_bar_app_xpath, locator_type='xpath')
        self.driver.implicitly_wait(1)
    
    def click_menu_bar_elem_sequentialy(self, locator, locator_type='xpath'):
        """Click on element in the side menu sequentially by index"""
        self.click_element(locator=locator, locator_type=locator_type)
        self.driver.implicitly_wait(1)
        #Back button click
        self.click_element(locator='//android.widget.ImageButton[@resource-id="com.ajaxsystems:id/back"]', 
                           locator_type=locator_type)
        self.click_side_menu_bar()