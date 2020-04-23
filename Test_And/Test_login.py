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
desired_caps['app']='/Users/cady/Downloads/手机梵讯.apk'
desired_caps['appPackage']='com.fooww.soft.android.Presentation'
desired_caps['appActivity']='.SplashScreenActivity'
# desired_caps['fullReset']= "true"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
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
    ele=geteleById(id)
    ele.click()

def sendkeyseleById(id,value):
    text_field=geteleById(id)
    text_field.clear()
    text_field.send_keys(value)


if __name__ == "__main__":
    always_allow(driver,3)
    driver.implicitly_wait(20)
    clickeleById("com.fooww.soft.android.Presentation:id/btn_splash_skip")
    driver.implicitly_wait(10)
    sendkeyseleById("com.fooww.soft.android.Presentation:id/etEmail","13000000033")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/etPassword","1234567:pUblic")
    clickeleById("com.fooww.soft.android.Presentation:id/btnLogin")
    time.sleep(10)
    driver.quit()





