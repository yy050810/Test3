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


if __name__ == "__main__":
    # 处理系统权限弹框
    driver.implicitly_wait(5)
    always_allow(driver, 1)
    driver.implicitly_wait(1)
    # 点击【客源】tab
    clickeleById("com.fooww.soft.android.Presentation:id/demand_badge")
    driver.implicitly_wait(3)
    # 点击【添加客源】
    clickeleById("com.fooww.soft.android.Presentation:id/iv_title_bar_add")
    clickeleByXpath("//*[@text='添加新客源']")
    # 填写客源姓名
    sendkeyseleById("com.fooww.soft.android.Presentation:id/et_demand_customer_name", "测试顾客And")
    # 填写电话
    sendkeyseleById("com.fooww.soft.android.Presentation:id/demand_view_phone_0", "13501300333")
    # 填写总价
    sendkeyseleById("com.fooww.soft.android.Presentation:id/edit_start", "0")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/edit_end", "500")
    time.sleep(1)
    # 向下滑动
    swipe_up(1)
    # 填写户型
    sendkeyseleById("com.fooww.soft.android.Presentation:id/et_demand_room_count", "2")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/et_demand_hall_count", "1")
    # 选择区县
    clickeleById("com.fooww.soft.android.Presentation:id/tv_demand_district_edit")
    driver.implicitly_wait(3)
    clickeleByXpath("//*[@text='日喀则市']")
    driver.implicitly_wait(3)
    # 添加意向小区
    clickeleById("com.fooww.soft.android.Presentation:id/tv_demand_add_intention_community")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/mEtSearch", "矿业第一安居")
    driver.implicitly_wait(3)
    clickeleById("com.fooww.soft.android.Presentation:id/tvCommunity")
    driver.implicitly_wait(3)
    # 保存
    clickeleByXpath("//*[@text='保存']")
    # 查看客源详情
    driver.implicitly_wait(5)
    clickeleByXpath("//*[@text='测试顾客And']")
    driver.implicitly_wait(5)
    # 查看客源电话
    clickeleById("com.fooww.soft.android.Presentation:id/iv_call_phone")
    # 返回
    driver.keyevent(4)
    # 删除客源
    TouchAction(driver).long_press(geteleByXpath("//*[@text='测试顾客And']")).perform()
    clickeleByXpath("//*[@text='删除']")
    clickeleById("com.fooww.soft.android.Presentation:id/md_buttonDefaultPositive")
    # 查询
    driver.implicitly_wait(5)
    clickeleById("com.fooww.soft.android.Presentation:id/iv_title_bar_filter")
    driver.implicitly_wait(3)
    clickeleById("com.fooww.soft.android.Presentation:id/etUserOwner")
    clickeleByXpath("//*[@text='王明Wangmin']")
    driver.implicitly_wait(3)
    clickeleById("com.fooww.soft.android.Presentation:id/etBusinessState")
    clickeleByXpath("//*[@text='状态不限']")
    clickeleById("com.fooww.soft.android.Presentation:id/btnConfirmCondition")
    time.sleep(10)
