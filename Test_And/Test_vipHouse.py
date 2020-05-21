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
    text_field.send_keys(value)


def sendkeyseleByXpath(path, value):
    '''
    向输入框输入文字
    :param path: path
    :param value:
    :return:
    '''
    text_field = geteleByXpath(path)
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

def btn_close(id):
    '''
    处理升级弹框
    :param id:【跳过】按钮id
    :return:
    '''
    try:
        ele = geteleById(id)
        ele.click()
    except:
        pass


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
    #处理广告点击【跳过】
    driver.implicitly_wait(10)
    btn_close("com.fooww.soft.android.Presentation:id/btn_close")
    # 处理系统权限弹框
    driver.implicitly_wait(5)
    always_allow(driver, 1)
    driver.implicitly_wait(1)
    # 点击【发现】tab
    clickeleById("com.fooww.soft.android.Presentation:id/find_badge")
    # 点击【个人房源】
    clickeleByXpath("//*[@text='个人房源']")
    # 点击【个人二手房】
    clickeleById("com.fooww.soft.android.Presentation:id/rl_self_second")
    # 点击第一个不为【已导入】的房源
    eles = driver.find_elements_by_xpath(
        "//*[@resource-id='com.fooww.soft.android.Presentation:id/rv_house_list']/android.widget.RelativeLayout[not(.//*[@text='已导入'])]")
    eles[0].click()
    # 查看电话
    driver.implicitly_wait(1)
    clickeleById("com.fooww.soft.android.Presentation:id/ivCallPhone_text")
    swipe_up(1)
    # 查看图片
    clickeleById("com.fooww.soft.android.Presentation:id/tvImage")
    time.sleep(3)
    # 返回
    driver.keyevent(4)
    # 导入
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='导入']")
    # 点击【保存】
    clickeleById("com.fooww.soft.android.Presentation:id/TitleBarGuideForward")
    # 个人房源搜索
    clickeleById("com.fooww.soft.android.Presentation:id/mEtSearch")
    driver.implicitly_wait(10)
    sendkeyseleById("com.fooww.soft.android.Presentation:id/mEtSearch", "新苑")
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='搜索']")
    time.sleep(3)
    # 返回
    driver.keyevent(4)
    driver.keyevent(4)
    # 点击【房源】
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/house_badge")
    # 点击房源列表第一套房源（刚刚导入）
    driver.implicitly_wait(10)
    houses = driver.find_elements_by_xpath(
        "//*[@resource-id='com.fooww.soft.android.Presentation:id/rv_house_list']/android.widget.LinearLayout")
    houses[0].click()
    # 下滑
    swipe_up(1)
    time.sleep(10)
    driver.quit()
