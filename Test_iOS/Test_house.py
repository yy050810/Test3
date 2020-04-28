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


def sendkeyseleById(id, value):
    text_field = geteleById(id)
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
    clickeleById("icon houseList add")
    # 点击【录入房源】
    target_click(117, 515)
    clickeleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请选择'")
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请输入小区关键字或拼音'", "一期")
    driver.implicitly_wait(2)
    # 搜索小区
    clickeleById("颐和轩一期")
    # 填写总价
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请填写'", "500")
    # 填写面积
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请填写'", "80")
    # 选择朝向
    clickeleByPredicate("type == 'XCUIElementTypeTextField' AND value == '其他'")
    clickeleById("东西")
    clickeleById("确定")
    # 选择装修情况
    clickeleByPredicate("type == 'XCUIElementTypeTextField' AND value == '毛坯'")
    clickeleById("精装")
    clickeleById("确定")
    # 向下滑动
    driver.execute_script('mobile: scroll', {'direction': 'down'})
    # 点击照片
    clickeleById("icon right camera")
    clickeleById("本地照片")
    # 处理照片访问权限
    photo_handle_permission(2)
    # 选择并上传图片
    clickeleByXpath("(//XCUIElementTypeImage[@name='TZImagePickerController.bundle/photo_def_photoPickerVc.png'])[1]")
    clickeleById("完成")
    driver.implicitly_wait(10)
    clickeleById("icon back left")
    driver.implicitly_wait(5)
    clickeleById("保存")
    driver.implicitly_wait(10)
    # 查看房源详情
    clickeleByPredicate("type == 'XCUIElementTypeStaticText' AND value CONTAINS '颐和轩一期'")
    # 查看业主信息
    clickeleById("icon_tabbar_customerInfo")
    # 返回房源详情
    clickeleByPredicate("type == 'XCUIElementTypeButton' AND name == 'icon back left'")
    # 返回房源列表
    clickeleByPredicate("type == 'XCUIElementTypeButton' AND name == 'icon back left'")
    # 删除房源
    toLeftSwipeByPredicate("type == 'XCUIElementTypeStaticText' AND value CONTAINS '颐和轩一期'")
    clickeleByPredicate("type == 'XCUIElementTypeButton' AND name == '删除'")
    clickeleById("确定")
    # 搜索房源
    driver.implicitly_wait(3)
    clickeleById("经纪人/电话/小区/编号/门牌")
    driver.implicitly_wait(1)
    sendkeyseleById("经纪人/电话/小区/编号/门牌", "测试")
    time.sleep(15)
    driver.quit()
