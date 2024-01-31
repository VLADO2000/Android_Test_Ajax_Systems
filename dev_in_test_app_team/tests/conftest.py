
import subprocess
import time


import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

from utils.android_utils import android_get_desired_capabilities



APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'

@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()
    
  


@pytest.fixture(scope='session')
def driver(appium_service):
    options = UiAutomator2Options()
    options.load_capabilities(android_get_desired_capabilities())
    driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

