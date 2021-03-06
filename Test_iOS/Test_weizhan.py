import os
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '12.4'
desired_caps['deviceName'] = 'iPhone 7'
desired_caps['app'] = 'com.fooww.softiphone'
desired_caps['udid'] = '478c4f8a26209f259d4f7445a68173f8e65d1638'
desired_caps['noReset'] = True  # 不重装应用

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def geteleByPredicate(con):
    '''
    通过ByPredicate方式获得元素
    :param con: condition
    :return: 元素
    '''
    ele = driver.find_element_by_ios_predicate(con)
    return ele


def geteleById(id):
    '''
    通过id方法获得元素
    :param id: id
    :return: 元素
    '''
    ele = driver.find_element_by_accessibility_id(id)
    return ele


def geteleByXpath(path):
    '''
    通过xpath方法获得元素
    :param path:
    :return: 元素
    '''
    ele = driver.find_element_by_xpath(path)
    return ele


def clickeleByPredicate(con):
    ele = geteleByPredicate(con)
    ele.click()


def clickeleById(id):
    ele = geteleById(id)
    ele.click()


def clickeleByXpath(path):
    ele = geteleByXpath(path)
    ele.click()


def sendkeyseleByPredicate(con, value):
    text_field = geteleByPredicate(con)
    text_field.clear()
    text_field.send_keys(value)


def toLeftSwipeByPredicate(con):
    ele = geteleByPredicate(con)
    driver.execute_script("mobile:swipe", {"direction": "left", 'element': ele, "duration": 1})


def toLeftSwipeById(id):
    ele = geteleById(id)
    driver.execute_script("mobile:swipe", {"direction": "left", 'element': ele, "duration": 1})


def toLeftSwipeByXpath(path):
    ele = geteleByXpath(path)
    driver.execute_script("mobile:swipe", {"direction": "left", 'element': ele, "duration": 1})


def sendkeyseleById(id, value):
    text_field = geteleById(id)
    text_field.clear()
    text_field.send_keys(value)


def sendkeyseleByXpath(path, value):
    text_field = geteleByXpath(path)
    text_field.clear()
    text_field.send_keys(value)


def target_click(x1, y1):
    '''
    :param self:
    :param x1: x1,y1为编写脚本时适用设备的实际坐标
    :param y1:
    :return:
    '''
    a1 = x1 / 374
    b1 = y1 / 667
    # 获取当前手机屏幕大小X,Y
    X = driver.get_window_size()['width']
    Y = driver.get_window_size()['height']
    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    driver.execute_script("mobile: tap", {"x": a1 * X, "y": b1 * Y})


def drag(ele, time):
    '''
    下拉操作
    :param ele:
    :param time:
    :return:
    '''
    a = 0.5
    b1 = 70 / 667
    b2 = 450 / 667
    # 获取当前手机屏幕大小X,Y
    X = driver.get_window_size()['width']
    Y = driver.get_window_size()['height']
    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    driver.execute_script("mobile:dragFromToForDuration",
                          {"duration": time, "element": ele, "fromX": a * X, "fromY": b1 * Y, "toX": a * X,
                           "toY": b2 * Y})


def photo_handle_permission(time):
    '''
    权限处理
    :param time: 等待时间
    :return:
    '''
    driver.implicitly_wait(time)
    if (len(driver.find_elements_by_name("好")) > 0):
        driver.find_element_by_name("好").click()
    else:
        pass


def get_size():
    '''
    获取屏幕尺寸
    :return: 长宽
    '''
    size = driver.get_window_size()
    x = size['width']
    y = size['height']
    return x, y


if __name__ == "__main__":
    driver.implicitly_wait(10)
    # 点击【消息】tab
    clickeleByXpath("//XCUIElementTypeButton[@name='消息']")
    driver.implicitly_wait(3)
    clickeleById("微站客户")
    driver.implicitly_wait(3)
    clickeleById("访客动态")
    # 向下滑动
    driver.execute_script('mobile: scroll', {'direction': 'down'})
    # 点击【分享获客】
    clickeleById("分享获客")
    driver.implicitly_wait(3)
    # 点击【立即分享】
    clickeleById("立即分享")
    time.sleep(1)
    # 下拉分享
    drag(geteleById("租房"), 0.4)
    # 退出介绍页
    clickeleById("icon back left")
    drag(geteleById("租房"), 0.4)
    driver.implicitly_wait(3)
    clickeleById("生成房源单")
    # 点击【分享】
    clickeleByXpath("//XCUIElementTypeButton[@name=' 分享']")
    # 选择【微信】
    driver.implicitly_wait(3)
    clickeleById("wx icon")
    # 选择微信要分享的人
    driver.implicitly_wait(10)
    clickeleByPredicate("type == 'XCUIElementTypeStaticText' AND value == 'Cady' AND name == 'Cady'")
    # 点击【发送】
    driver.implicitly_wait(10)
    clickeleById("发送")
    # 点击【返回手机梵讯】
    driver.implicitly_wait(10)
    clickeleById("返回手机梵讯")

    time.sleep(10)
    driver.quit()
