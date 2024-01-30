from appium.webdriver.common.appiumby import AppiumBy
import time


def test_first_page_correctness(user_login_fixture):
    login = user_login_fixture.find_element(AppiumBy.XPATH, 
            '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
    
    #Todo
    #login.click()
    # login.send_keys()
    #Todo
    
    assert login.text == 'Log In'

def test_login_page_transfer(user_login_fixture):
    login = user_login_fixture.find_element(AppiumBy.XPATH, 
            '//android.widget.FrameLayout[@resource-id="com.ajaxsystems:id/authHelloLogin"]')
    user_login_fixture.click_element(login)
    time.sleep(3)

    email = user_login_fixture.find_element(AppiumBy.XPATH, 
            '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]')
    user_login_fixture.send_keys('qa.ajax.app.automation@gmail.com', email)

    passw = user_login_fixture.find_element(AppiumBy.XPATH, 
            '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]')
    user_login_fixture.send_keys('qa_automation_password', passw)

    forg_pss = user_login_fixture.find_element(AppiumBy.XPATH, 
            '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Forgot password?"]')
    
    auth_login = user_login_fixture.find_element(AppiumBy.XPATH, 
            '//android.widget.FrameLayout[@resource-id="com.ajaxsystems:id/authLogin"]')
    user_login_fixture.click_element(auth_login)
    time.sleep(5)

    
    assert (email.get_attribute('clickable'))
    assert (passw.get_attribute('password'))
    assert (forg_pss.get_attribute('displayed'))
    assert forg_pss.text == 'Forgot password?'


    
    
    
    
    

    

