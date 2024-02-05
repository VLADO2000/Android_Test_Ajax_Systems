import time
import pytest

from appium.webdriver.common.appiumby import AppiumBy 
from selenium.webdriver.common.by import By 



def test_welcome_login_page(user_login_fixture):
    assert (user_login_fixture.assert_hello_login_btn_exists())

def test_navigation_toward_auth_page(user_login_fixture):
    user_login_fixture.navigate_to_input_login_page()
    assert (user_login_fixture.assert_hello_login_navigation_correctness())

@pytest.mark.parametrize(
        "email, password",
        [
         
         pytest.param('invader_manualqa@mqdb.ua', 'justletmein', 
                      marks=pytest.mark.xfail(
                              reason="Incorrect credentials")),
        pytest.param('qa.ajax.app.automation@gmail.com', 'justletmein', 
                      marks=pytest.mark.xfail(
                              reason="Incorrect password")),
        
        pytest.param('invader_manualqa@mqdb.ua', 'qa_automation_password', 
                      marks=pytest.mark.xfail(
                              reason="Incorrect email")),
        ('qa.ajax.app.automation@gmail.com', 'qa_automation_password'),
        ],
)
def test_user_authorization(user_login_fixture, email, password):
    email_input_field = user_login_fixture.get_email_login_field()
    if email_presence := user_login_fixture.get_text(email_input_field):
        user_login_fixture.clear_field(email_input_field)

    password_input_field = user_login_fixture.get_password_login_field()
    user_login_fixture.send_info(text=password, element=password_input_field)
    user_login_fixture.send_info(text=email, element=email_input_field)

    user_login_fixture.click_login_auth_submit()

    
    

    


    
    
    
    
    

    

