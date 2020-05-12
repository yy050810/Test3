import os
from appium import webdriver
import time

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


if __name__ == "__main__":
    driver.implicitly_wait(10)
    # 点击【客源】tab
    clickeleById("客源")
    # 点击【添加新客源】
    clickeleById("icon Custom add")
    clickeleById("添加新客源")
    driver.implicitly_wait(10)
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请填写姓名'", "测试顾客ios")
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请填写电话号码'", "13501500555\n")
    time.sleep(1)
    # 向下滑动
    driver.execute_script('mobile: scroll', {'direction': 'down'})
    # 选择区县
    driver.implicitly_wait(10)
    clickeleByXpath("(//XCUIElementTypeStaticText[@name='不限'])[1]")
    driver.implicitly_wait(10)
    clickeleById("闸北")
    driver.implicitly_wait(10)
    # 添加意向小区
    clickeleById("添加")
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请输入小区关键字或拼音'", "测试闸北")
    driver.implicitly_wait(10)
    clickeleByPredicate("type == 'XCUIElementTypeStaticText' AND value == '测试闸北'")
    driver.implicitly_wait(10)
    # 保存
    clickeleById("保存")
    driver.implicitly_wait(10)
    # 查看客源详情
    clickeleByXpath("//XCUIElementTypeStaticText[@name='测试顾客ios']")
    driver.implicitly_wait(10)
    # 查看客源电话
    clickeleById("call on")
    clickeleById("icon back left")
    driver.implicitly_wait(10)
    # 删除客源
    toLeftSwipeByXpath("//XCUIElementTypeStaticText[@name='测试顾客ios']")
    clickeleByPredicate("type == 'XCUIElementTypeButton' AND name == '删除'")
    clickeleById("确定")
    # 查询
    driver.implicitly_wait(10)
    clickeleById("icon customer search")
    clickeleByXpath("(//XCUIElementTypeStaticText[@name='不限'])[1]")
    clickeleById("尼克斯1115")
    clickeleById("全部有效")
    clickeleById("全部不限")
    driver.implicitly_wait(10)
    clickeleByXpath("(//XCUIElementTypeButton[@name='查询'])[1]")

    time.sleep(10)
    driver.quit()
