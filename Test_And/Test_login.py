import os
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = '7XBRX19426001121'
desired_caps['app'] = '/Users/cady/Downloads/手机梵讯.apk'
desired_caps['appPackage'] = 'com.fooww.soft.android.Presentation'
desired_caps['appActivity'] = '.SplashScreenActivity'
# desired_caps['fullReset']= True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def always_allow(driver, number=5):
    '''
    允许权限弹窗处理
    :param driver:
    :param number: 点击"允许"次数
    :return:
    '''
    for i in range(3):
        loc = ("xpath", "//*[@text='始终允许']")
        try:
            e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
            e.click()
        except:
            pass


def geteleById(id):
    ele = driver.find_element_by_id(id)
    return ele


def clickeleById(id):
    ele = geteleById(id)
    ele.click()


def sendkeyseleById(id, value):
    text_field = geteleById(id)
    text_field.clear()
    text_field.send_keys(value)


if __name__ == "__main__":
    # 处理3个权限弹窗
    always_allow(driver, 3)
    # 点击【跳过】
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/btn_splash_skip")
    driver.implicitly_wait(10)
    # 输入用户名和密码
    sendkeyseleById("com.fooww.soft.android.Presentation:id/etEmail", "15900000001")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/etPassword", "1234567:pUblic")
    clickeleById("com.fooww.soft.android.Presentation:id/btnLogin")
    driver.implicitly_wait(10)
    # 处理1个权限弹窗
    always_allow(driver, 1)
    time.sleep(10)
    driver.quit()
