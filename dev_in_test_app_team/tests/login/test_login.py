import time

def test_welcome_login_page(user_login_fixture):
    assert (user_login_fixture.assert_hello_login_btn_exists())

def test_navigation_toward_auth_page(user_login_fixture):
    user_login_fixture.navigate_to_input_login_page()
    assert (user_login_fixture.assert_hello_login_navigation_correctness())

def test_credetials_input(user_login_fixture):
    user_login_fixture.input_email_password(email='qa.ajax.app.automation@gmail.com',
                                            password='qa_automation_password')
    
    user_login_fixture.driver.implicitly_wait(2)

    email_auto_input = user_login_fixture.find_element(locator=
                                                       user_login_fixture._email_login_field_xpath)
    
    email_auto_input_text = user_login_fixture.get_text(email_auto_input)
    user_login_fixture.driver.implicitly_wait(2)

    user_login_fixture.click_login_auth_submit()
    user_login_fixture.driver.implicitly_wait(2)

    assert email_auto_input_text == 'qa.ajax.app.automation@gmail.com'


    
    
    
    
    

    

