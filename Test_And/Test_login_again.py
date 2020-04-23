import os
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

desired_caps=dict()
desired_caps['platformName']='Android'
desired_caps['platformVersion']='8.1.0'
desired_caps['deviceName']='7XBRX19426001121'
desired_caps['appPackage']='com.fooww.soft.android.Presentation'
desired_caps['appActivity']='.SplashScreenActivity'
desired_caps['noReset'] = True # 不重装应用

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

if __name__ == "__main__":
    time.sleep(20)
    driver.quit()





