import os
from appium import webdriver
import time

desired_caps = dict()
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '12.4'
desired_caps['deviceName'] = 'iPhone 7'
desired_caps['app'] = 'com.fooww.softiphone'
desired_caps['udid'] = '478c4f8a26209f259d4f7445a68173f8e65d1638'
desired_caps['locationServicesEnabled'] = True
desired_caps['locationServicesAuthorized'] = True
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


def clickeleByPredicate(con):
    ele = geteleByPredicate(con)
    ele.click()


def clickeleById(id):
    ele = geteleById(id)
    ele.click()


def sendkeyseleByPredicate(con, value):
    text_field = geteleByPredicate(con)
    text_field.clear()
    text_field.send_keys(value)


def sendkeyseleById(id, value):
    text_field = geteleById(id)
    text_field.clear()
    text_field.send_keys(value)


def location_handle_permission():
    '''
    权限处理
    :return:
    '''
    if (len(driver.find_elements_by_name("始终允许")) > 0):
        driver.find_element_by_name("始终允许").click()
    else:
        pass


if __name__ == "__main__":
    driver.switch_to.alert.accept()
    driver.implicitly_wait(10)
    clickeleById("guid clickSkip")
    driver.implicitly_wait(10)
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请输入您的梵讯账号/邮箱/手机号码'", "15900000001")
    sendkeyseleByPredicate("type == 'XCUIElementTypeSecureTextField' AND value == '请输入您的密码'", "1234567:pUblic")
    clickeleById("登录")
    # 位置权限弹窗在这里出现并处理
    driver.implicitly_wait(10)
    location_handle_permission()
    driver.implicitly_wait(10)
    clickeleById("icon PopupWindow Quit")
    time.sleep(5)
    driver.quit()
