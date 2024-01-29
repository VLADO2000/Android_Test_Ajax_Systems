def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'UiAutomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'deviceName':'emulator_5554',
        'platformVersion': '14.0',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': '11bd127d',
        'app':'/Users/sharkeee/Desktop/Ajax Security System_2.35_Apkpure.apk',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
      
}
