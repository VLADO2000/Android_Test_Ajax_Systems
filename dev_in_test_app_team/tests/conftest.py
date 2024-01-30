
import subprocess
import time


import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.android_utils import android_get_desired_capabilities


# @pytest.fixture(scope='session')
# def run_appium_server():
#     subprocess.Popen(
#         ['appium', '-a', '0.0.0.0', '-p', '4723'],
#         stdout=subprocess.DEVNULL,
#         stderr=subprocess.DEVNULL,
#         stdin=subprocess.DEVNULL,
#         shell=True
#     )
#     time.sleep(5)
    
  


@pytest.fixture(scope='session')
def driver():
    options = UiAutomator2Options()
    options.load_capabilities(android_get_desired_capabilities())
    driver = webdriver.Remote('http://localhost:4723', options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

