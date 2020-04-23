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
    '''
    通过id查找元素
    :param id:
    :return: 元素
    '''
    ele = driver.find_element_by_id(id)
    return ele

def geteleByXpath(path):
    '''
    通过xpath查找元素
    :param path:
    :return: 元素
    '''
    ele = driver.find_element_by_xpath(path)
    return ele

def clickeleById(id):
    '''
    ById点击方法
    :param id:
    :return:
    '''
    ele=geteleById(id)
    ele.click()

def clickeleByXpath(path):
    '''
    ByXpath点击方法
    :param path:
    :return:
    '''
    ele=geteleByXpath(path)
    ele.click()

def sendkeyseleById(id,value):
    '''
    向输入框输入文字
    :param id:
    :param value:
    :return:
    '''
    text_field=geteleById(id)
    text_field.clear()
    text_field.send_keys(value)


if __name__ == "__main__":
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/main_floating_action_bar")
    clickeleByXpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View[1]")






