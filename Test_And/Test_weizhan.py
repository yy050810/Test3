import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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
desired_caps['appPackage'] = 'com.fooww.soft.android.Presentation'
desired_caps['appActivity'] = '.SplashScreenActivity'
desired_caps['noReset'] = True  # 不重装应用

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
    ele = geteleById(id)
    ele.click()


def clickeleByXpath(path):
    '''
    ByXpath点击方法
    :param path:
    :return:
    '''
    ele = geteleByXpath(path)
    ele.click()


def sendkeyseleById(id, value):
    '''
    向输入框输入文字
    :param id:
    :param value:
    :return:
    '''
    text_field = geteleById(id)
    text_field.clear()
    text_field.send_keys(value)


def sendkeyseleByXpath(path, value):
    '''
    向输入框输入文字
    :param path: path
    :param value:
    :return:
    '''
    text_field = geteleByXpath(path)
    text_field.clear()
    text_field.send_keys(value)


def get_size():
    '''
    获取屏幕尺寸
    :return: 长宽
    '''
    size = driver.get_window_size()
    x = size['width']
    y = size['height']
    return x, y


def swipe_up(count):
    '''
    向下滑动方法
    :param count:滑动次数
    :return:
    '''
    x1 = get_size()[0] * 0.5
    y1 = get_size()[1] * 0.85
    y2 = get_size()[1] * 0.15
    for i in range(count):
        time.sleep(1)
        driver.swipe(x1, y1, x1, y2)


def drag(driver, ele, time):
    '''
    下拉操作
    :param ele:
    :param time:
    :return:
    '''
    a = 0.5
    b2 = 450 / 667
    # 获取当前手机屏幕大小X,Y
    X = driver.get_window_size()['width']
    Y = driver.get_window_size()['height']
    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    TouchAction(driver).press(ele).wait(time).move_to(x=a * X, y=b2 * Y).release().perform();


if __name__ == "__main__":
    # 处理系统权限弹框
    driver.implicitly_wait(5)
    always_allow(driver, 1)
    driver.implicitly_wait(1)
    # 点击【消息】tab
    clickeleById("com.fooww.soft.android.Presentation:id/message_badge")
    driver.implicitly_wait(3)
    clickeleByXpath("//*[@text='微站客户']")
    # 点击【访客动态】
    driver.implicitly_wait(3)
    clickeleById("com.fooww.soft.android.Presentation:id/customer_dynm")
    # 向下滑动
    swipe_up(2)
    # 点击【分享获客】
    clickeleById("com.fooww.soft.android.Presentation:id/customer_share")
    # 点击【立即分享】
    clickeleById("com.fooww.soft.android.Presentation:id/sg_submit")
    # 下拉分享
    time.sleep(1)
    drag(driver, geteleByXpath("//*[@text='租房']"), 500)
    # 退出介绍页
    driver.keyevent(4)
    # 再次下拉分享
    time.sleep(3)
    drag(driver, geteleByXpath("//*[@text='租房']"), 500)
    driver.implicitly_wait(3)
    clickeleById("com.fooww.soft.android.Presentation:id/mBtCollect")
    # 点击【分享】
    clickeleByXpath("//*[@text='分享']")
    # 选择【微信】
    clickeleByXpath("//*[@text='微信好友']")
    # 选择微信要分享的人
    clickeleByXpath("//*[@text='Cady']")
    # 点击【发送】
    driver.implicitly_wait(3)
    clickeleByXpath("//*[@text='分享']")
    # 点击【返回手机梵讯】
    clickeleByXpath("//*[@text='返回手机梵讯']")

    time.sleep(10)
    driver.quit()
