import os
from appium import webdriver
import time


desired_caps=dict()
desired_caps['platformName']='iOS'
desired_caps['platformVersion']='12.4'
desired_caps['deviceName']='iPhone 7'
desired_caps['app']='com.fooww.softiphone'
desired_caps['udid']='478c4f8a26209f259d4f7445a68173f8e65d1638'
desired_caps['noReset'] = True # 不重装应用

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

if __name__ == "__main__":
    time.sleep(20)
    driver.quit()
