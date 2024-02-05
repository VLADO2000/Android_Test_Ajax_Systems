import pytest

from framework.login_page import LoginPage
from framework.homeHub_page import HomeHubPage

@pytest.fixture(scope='session')
def authentication_driver(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_input_login_page()
    email_input = login_page.get_email_login_field()
    password_input = login_page.get_password_login_field()
    login_page.send_info(text='qa.ajax.app.automation@gmail.com', 
                         element=email_input)
    login_page.send_info(text='qa_automation_password',
                         element=password_input)
    login_page.click_login_auth_submit()
    yield driver

@pytest.fixture(scope='session')
def homehub_fixture(authentication_driver):
    home = HomeHubPage(authentication_driver)
    
    yield home
