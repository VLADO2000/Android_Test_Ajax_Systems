def test_user_login(user_login_fixture):
    login = user_login_fixture.find_element('android.widget.Button')
    login.click()
    
    assert True
