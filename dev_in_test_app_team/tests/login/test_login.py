import time

_add_hub_after_login_xpath = '//android.view.ViewGroup[@resource-id="com.ajaxsystems:id/hubAdd"]'

def test_welcome_login_page(user_login_fixture):
    assert (user_login_fixture.assert_hello_login_btn_exists())

def test_navigation_toward_auth_page(user_login_fixture):
    user_login_fixture.navigate_to_input_login_page()
    assert (user_login_fixture.assert_hello_login_navigation_correctness())

def test_credetials_input(user_login_fixture):
    user_login_fixture.input_email_password(email='qa.ajax.app.automation@gmail.com',
                                            password='qa_automation_password')
    
    user_login_fixture.driver.implicitly_wait(2)

    user_login_fixture.click_login_auth_submit()

    assert (user_login_fixture.is_element_present(locator=_add_hub_after_login_xpath,
                                                  locator_type='xpath'))


    
    
    
    
    

    

