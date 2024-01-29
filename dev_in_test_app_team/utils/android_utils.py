def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'iautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': '11bd127d',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
        # 'autoGrantPermissions': True,
        # 'automationName': 'iautomator2',
        # 'newCommandTimeout': 500,
        # 'noSign': True,
        # 'platformName': 'Android',
        # 'platformVersion': '10',
        # 'resetKeyboard': True,
        # 'systemPort': 8301,
        # 'takesScreenshot': True,
        # 'udid': '11bd127d',
        # 'appPackage': 'com.ajaxsystems',
        # 'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
