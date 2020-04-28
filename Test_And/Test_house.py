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
    driver.implicitly_wait(10)
    # 点击【+】
    clickeleById("com.fooww.soft.android.Presentation:id/main_floating_action_bar")
    # 点击【录入房源】
    clickeleByXpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View[1]")
    # 点击【小区】
    clickeleById("com.fooww.soft.android.Presentation:id/tv_house_add_row_select_value")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/mEtSearch", "一期")
    driver.implicitly_wait(10)
    # 搜索小区
    clickeleByXpath("//*[@text='颐和轩一期']")
    driver.implicitly_wait(10)
    # 填写总价
    sendkeyseleByXpath("//*[@text='请填写']", "500")
    sendkeyseleByXpath("//*[@text='请填写']", "80")
    # 选择朝向
    clickeleByXpath("//*[@text='其他']")
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='东西']")
    clickeleByXpath("//*[@text='确定']")
    # 选择装修
    clickeleByXpath("//*[@text='毛坯']")
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='精装']")
    clickeleByXpath("//*[@text='确定']")
    # 向上滑动
    time.sleep(1)
    swipe_up(2)
    driver.implicitly_wait(10)
    # 点击照片
    clickeleById("com.fooww.soft.android.Presentation:id/row_add_edit_house_take_photo")
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='本地图片']")
    # 处理照片访问权限
    driver.implicitly_wait(10)
    always_allow(driver, 1)
    # 选择并上传图片
    clickeleById("com.fooww.soft.android.Presentation:id/check_view")
    clickeleByXpath("//*[@text='使用1']")
    time.sleep(3)
    # 返回
    driver.keyevent(4)
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='保存']")
    driver.implicitly_wait(10)
    # 查看房源详情
    clickeleByXpath("//*[@text='颐和轩一期']")
    # 查看业主信息
    clickeleById("com.fooww.soft.android.Presentation:id/ivOwner")
    time.sleep(3)
    # 返回房源详情
    driver.keyevent(4)
    # 返回房源列表
    driver.keyevent(4)
    # 删除房源
    TouchAction(driver).long_press(geteleByXpath("//*[@text='颐和轩一期']")).perform()
    clickeleByXpath("//*[@text='删除']")
    clickeleById("com.fooww.soft.android.Presentation:id/md_buttonDefaultPositive")
    # 搜索房源
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/et_search_bar")
    driver.implicitly_wait(10)
    sendkeyseleById("com.fooww.soft.android.Presentation:id/mEtKeyword", "测试吧")
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/mTvKeyword")
    time.sleep(10)
    driver.quit()
