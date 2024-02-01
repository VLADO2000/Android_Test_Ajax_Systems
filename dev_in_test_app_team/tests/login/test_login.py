import time
import pytest

_add_hub_after_login_xpath = '//android.view.ViewGroup[@resource-id="com.ajaxsystems:id/hubAdd"]'

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
        ('qa.ajax.app.automation@gmail.com', 'qa_automation_password'),
        pytest.param('invader_manualqa@mqdb.ua', 'qa_automation_password', 
                      marks=pytest.mark.xfail(
                              reason="Incorrect email")),
        ],
)
def test_user_authorization(user_login_fixture, email, password):
    user_login_fixture.input_email_password(email=email,
                                            password=password)
    user_login_fixture.click_login_auth_submit()

    user_login_fixture.email_login_field_clear()
    user_login_fixture.passw_login_field_clear()

    #Gives ability to put valid credentials every where in parameters sequence, without it other test would be rejected 
    if (email == 'qa.ajax.app.automation@gmail.com' and 
        password =='qa_automation_password'):
        successful_login = user_login_fixture.is_element_present(locator=_add_hub_after_login_xpath,
                                                      locator_type='xpath')
        user_login_fixture.sign_out_and_navigate_to_login()

        assert successful_login


    
    
    
    
    

    

