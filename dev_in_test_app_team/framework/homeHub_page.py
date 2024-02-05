from appium.webdriver.common.appiumby import AppiumBy 
from selenium.webdriver.common.by import By 

from .page import Page

class HomeHubPage(Page):
    _add_new_hub_btn_xpath = '//android.view.ViewGroup[@resource-id="com.ajaxsystems:id/hubAdd"]'
    _menu_bar_app_xpath = '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
    _app_settings_xpath = '//android.view.View[@resource-id="com.ajaxsystems:id/settings"]'
    _sign_out_btn_xpath = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Sign Out"]'
   #Subbuttons
    _back_settings_btn_xpath='//android.widget.ImageButton[@resource-id="com.ajaxsystems:id/back"]'
    _side_bar_settings= '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]',
    _side_bar_help = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Help"]'
    _side_bar_icons_xpath = '//android.view.View[@resource-id="com.ajaxsystems:id/atomImage"]'
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def get_add_new_hub_btn(self):
        return self.find_element(locator=self._add_new_hub_btn_xpath, 
                                 locator_type=By.XPATH)
    
    
    def get_side_menu_bar(self):
        self.find_element(locator=self._menu_bar_app_xpath, 
                          locator_type=By.XPATH)
        self.driver.implicitly_wait(0)
    
    def get_sidebar_list(self):
        sidebar_list = self.find_elements_list(locator=self._side_bar_icons_xpath,
                                               locator_type=By.XPATH)
        return sidebar_list
    
    
        
        