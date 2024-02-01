import pytest

from framework.homeHub_page import HomeHubPage


@pytest.fixture(scope='session')
def homehub_fixture(driver):
    home = HomeHubPage(driver)
    home.navigate_to_input_login_page()
    home.email_login_field_clear()
    home.input_email_password(email='qa.ajax.app.automation@gmail.com', 
                              password='qa_automation_password')
    home.driver.implicitly_wait(1)
    home.click_login_auth_submit()
    yield home
