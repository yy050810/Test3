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
desired_caps['app'] = '/Users/cady/Downloads/Foowwphone.ipa'
desired_caps['locationServicesEnabled'] = True
desired_caps['locationServicesAuthorized'] = True
desired_caps['fullReset'] = True

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


def sendkeyseleByPredicate(con, value):
    text_field = geteleByPredicate(con)
    text_field.clear()
    text_field.send_keys(value)


def sendkeyseleById(id, value):
    text_field = geteleById(id)
    text_field.clear()
    text_field.send_keys(value)


def sendkeyseleByXpath(path, value):
    text_field = geteleByXpath(path)
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


def browsehouses(count):
    '''
    按房源列表顺序浏览房源
    :param count: 浏览次数
    :return:
    '''
    for i in range(count):
        driver.implicitly_wait(10)
        houses = driver.find_elements_by_xpath("//*[@type='XCUIElementTypeCell']")
        houses[i].click()
        time.sleep(1)
        driver.execute_script('mobile: scroll', {'direction': 'down'})
        time.sleep(1)
        driver.execute_script('mobile: scroll', {'direction': 'up'})
        time.sleep(1)
        clickeleByPredicate("type == 'XCUIElementTypeButton' AND label == 'icon back left'")


def toLeftSwipeByPredicate(con):
    ele = geteleByPredicate(con)
    driver.execute_script("mobile:swipe", {"direction": "left", 'element': ele, "duration": 1})


def toLeftSwipeByXpath(path):
    ele = geteleByXpath(path)
    driver.execute_script("mobile:swipe", {"direction": "left", 'element': ele, "duration": 1})


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

def vip_duplicate(time):
    '''
    权限处理
    :param time: 等待时间
    :return:
    '''
    driver.implicitly_wait(time)
    if (len(driver.find_elements_by_name("继续保存")) > 0):
        driver.find_element_by_name("继续保存").click()
    else:
        pass


def clickeleByXpath(path):
    ele = geteleByXpath(path)
    ele.click()


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




if __name__ == "__main__":
    # 登录
    driver.switch_to.alert.accept()
    driver.implicitly_wait(10)
    clickeleById("guid clickSkip")
    driver.implicitly_wait(10)
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请输入您的梵讯账号/邮箱/手机号码'", "15900000001")
    sendkeyseleByPredicate("type == 'XCUIElementTypeSecureTextField' AND value == '请输入您的密码'", "1234567:pUblic")
    clickeleById("登录")
    time.sleep(3)
    # 处理可能会出现的地理位置权限弹窗
    location_handle_permission()
    # 输入城市
    driver.implicitly_wait(10)
    sendkeyseleByPredicate("type == 'XCUIElementTypeSearchField' AND label == '请输入城市名称'", "上海")
    clickeleById("上海")
    # 如果前面弹窗没有出现就在这里出现并处理
    driver.implicitly_wait(20)
    location_handle_permission()

    ##导入个人房源常见操作
    driver.implicitly_wait(10)
    # 点击【发现】tab
    clickeleById("发现")
    # 点击【个人房源】
    clickeleById("个人房源")
    # 点击【个人二手房】
    clickeleById("个人二手房")
    # 点击第一个不为【已导入】的房源
    eles = driver.find_elements_by_xpath(
        "//*[@type='XCUIElementTypeTable']/XCUIElementTypeCell[not(.//*[@label='已导入'])]")
    eles[0].click()
    # 查看电话
    driver.implicitly_wait(1)
    clickeleById("call on")
    # 查看图片
    driver.execute_script('mobile: scroll', {'direction': 'down'})
    clickeleById("照片:")
    time.sleep(3)
    # 返回
    clickeleById("icon back left")
    # 导入
    clickeleById("导入")
    vip_duplicate(2)
    # 点击【保存】
    time.sleep(3)
    clickeleById("保存")
    driver.implicitly_wait(20)
    clickeleByPredicate("type =='XCUIElementTypeOther' AND label == '个人二手房详情'")
    clickeleById("icon back left")
    # 个人房源搜索
    driver.implicitly_wait(10)
    clickeleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请输入小区关键字'")
    time.sleep(3)
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请输入小区关键字'", "新苑")
    clickeleById("搜索")
    time.sleep(3)
    # 返回
    clickeleById("icon back left")
    clickeleById("icon back left")
    # 点击【房源】
    clickeleById("房源")
    # 点击房源列表第一套房源（刚刚导入）
    houses = driver.find_elements_by_xpath("//*[@type='XCUIElementTypeCell']")
    houses[0].click()
    # 下滑
    driver.execute_script('mobile: scroll', {'direction': 'down'})
    # 上滑
    time.sleep(1)
    driver.execute_script('mobile: scroll', {'direction': 'up'})
    # 返回
    driver.implicitly_wait(10)
    clickeleByPredicate("type =='XCUIElementTypeButton' AND name == 'icon back left'")

    ##房源常见操作
    # 浏览第1-3套房源
    driver.implicitly_wait(20)
    browsehouses(3)
    driver.implicitly_wait(10)
    # 点击【+】
    clickeleById("icon houseList add")
    # 点击【录入房源】
    target_click(117, 515)
    clickeleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请选择'")
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请输入小区关键字或拼音'", "闸北")
    driver.implicitly_wait(10)
    # 搜索小区
    clickeleById("闸北公房")
    # 填写总价
    driver.implicitly_wait(10)
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请填写'", "500")
    # 填写面积
    driver.implicitly_wait(10)
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextField' AND value == '请填写'", "80")
    # 选择朝向
    driver.implicitly_wait(10)
    clickeleByPredicate("type == 'XCUIElementTypeTextField' AND value == '其他'")
    clickeleById("东西")
    clickeleById("确定")
    # 选择装修情况
    driver.implicitly_wait(10)
    clickeleByPredicate("type == 'XCUIElementTypeTextField' AND value == '毛坯'")
    clickeleById("精装")
    clickeleById("确定")
    # 向下滑动
    driver.execute_script('mobile: scroll', {'direction': 'down'})
    # 点击照片
    driver.implicitly_wait(10)
    clickeleById("icon right camera")
    clickeleById("本地照片")
    # 处理照片访问权限
    photo_handle_permission(2)
    # 选择并上传图片
    clickeleByXpath("(//XCUIElementTypeImage[@name='TZImagePickerController.bundle/photo_def_photoPickerVc.png'])[1]")
    clickeleById("完成")
    driver.implicitly_wait(10)
    clickeleById("icon back left")
    driver.implicitly_wait(10)
    clickeleById("保存")
    # 查看房源详情
    driver.implicitly_wait(10)
    clickeleByPredicate("type == 'XCUIElementTypeStaticText' AND value == '闸北公房'")
    # 查看业主信息
    clickeleById("icon_tabbar_customerInfo")
    # 返回房源详情
    clickeleByPredicate("type == 'XCUIElementTypeButton' AND name == 'icon back left'")
    # 返回房源列表
    driver.implicitly_wait(10)
    clickeleByPredicate("type == 'XCUIElementTypeButton' AND name == 'icon back left'")
    # 删除房源
    toLeftSwipeByPredicate("type == 'XCUIElementTypeStaticText' AND value == '闸北公房'")
    clickeleByPredicate("type == 'XCUIElementTypeButton' AND name == '删除'")
    clickeleById("确定")
    # 搜索房源
    driver.implicitly_wait(10)
    clickeleById("经纪人/电话/小区/编号/门牌")
    driver.implicitly_wait(10)
    sendkeyseleById("经纪人/电话/小区/编号/门牌", "富贵小区")
    driver.implicitly_wait(10)
    clickeleById("搜索")
    driver.implicitly_wait(20)
    #清除搜索记录
    clickeleByPredicate("label == '清空全部搜索/筛选条件'")

    ##客源常见操作
    # 点击【客源】tab
    driver.implicitly_wait(10)
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
    # 匹配房源（选第一套）
    driver.implicitly_wait(10)
    clickeleByPredicate("type =='XCUIElementTypeButton' AND name == 'customer fitHouse'")
    driver.implicitly_wait(10)
    clickeleById("按需求信息匹配")
    driver.implicitly_wait(10)
    houses = driver.find_elements_by_xpath("//*[@type='XCUIElementTypeCell']")
    houses[0].click()
    driver.implicitly_wait(10)
    clickeleByPredicate("type =='XCUIElementTypeButton' AND name == '添加意向'")
    time.sleep(3)
    clickeleByPredicate("type =='XCUIElementTypeButton' AND label == 'icon back left'")
    clickeleById("icon attendance back")
    # 添加带看
    driver.implicitly_wait(10)
    clickeleById("icon button visit")
    driver.implicitly_wait(10)
    clickeleById("添加")
    # 添加带看房源
    driver.implicitly_wait(10)
    clickeleById('更多信息')
    houses = driver.find_elements_by_xpath("//*[@type='XCUIElementTypeCell']")
    houses[0].click()
    driver.implicitly_wait(10)
    clickeleById("确定")
    driver.implicitly_wait(10)
    sendkeyseleByPredicate("type == 'XCUIElementTypeTextView'", "添加房源情况…添加房源情况")
    clickeleById("确定")
    # 返回
    driver.implicitly_wait(20)
    clickeleByXpath("//XCUIElementTypeOther[@name='带看记录']")
    driver.implicitly_wait(10)
    clickeleById("icon back left")
    # 返回
    driver.implicitly_wait(10)
    clickeleByPredicate("type =='XCUIElementTypeOther' AND label == '二手房客源详情'")
    driver.implicitly_wait(10)
    clickeleById("icon back left")
    # 删除客源
    driver.implicitly_wait(20)
    toLeftSwipeByXpath("//XCUIElementTypeStaticText[@name='测试顾客ios']")
    clickeleByPredicate("type == 'XCUIElementTypeButton' AND name == '删除'")
    clickeleById("确定")
    # 查询
    driver.implicitly_wait(10)
    clickeleById("icon customer search")
    clickeleByXpath("(//XCUIElementTypeStaticText[@name='不限'])[1]")
    clickeleById("公司管理员")
    clickeleById("全部有效")
    clickeleById("全部不限")
    driver.implicitly_wait(10)
    clickeleByXpath("(//XCUIElementTypeButton[@name='查询'])[1]")

    ##消息常见操作
    driver.implicitly_wait(10)
    # 点击【消息】tab
    clickeleByXpath("//XCUIElementTypeButton[@name='消息']")
    # 点击【系统消息】
    driver.implicitly_wait(10)
    clickeleById("系统消息")
    driver.implicitly_wait(10)
    clickeleByPredicate("type =='XCUIElementTypeButton' AND name == 'icon back left'")
    # 点击【微站客户】
    driver.implicitly_wait(10)
    clickeleById("微站客户")
    driver.implicitly_wait(10)
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
    driver.implicitly_wait(15)
    clickeleByPredicate("type == 'XCUIElementTypeStaticText' AND value == 'Cady'")
    # 点击【发送】
    driver.implicitly_wait(10)
    clickeleById("发送")
    # 点击【返回手机梵讯】
    driver.implicitly_wait(10)
    clickeleById("返回手机梵讯")
    # 返回
    driver.implicitly_wait(10)
    clickeleById("icon back left")
    # 返回
    driver.implicitly_wait(10)
    clickeleById("icon attendance back")

    ## 个人常见操作
    driver.implicitly_wait(10)
    # 点击【我的】
    clickeleByXpath("//XCUIElementTypeButton[@name='我的']")
    # 向下滑动
    driver.execute_script('mobile: scroll', {'direction': 'down'})
    #点击【海报中心】
    clickeleById("海报中心")
    #切换tab
    driver.implicitly_wait(10)
    clickeleById("喜报")
    driver.implicitly_wait(10)
    clickeleById("拓客")
    driver.implicitly_wait(10)
    clickeleById("节日")
    driver.implicitly_wait(10)
    clickeleById("招聘")
    # 返回
    driver.implicitly_wait(10)
    clickeleById("icon back left")
    # 点击【合同】
    driver.implicitly_wait(10)
    clickeleById("合同")
    driver.implicitly_wait(10)
    clickeleById("icon back left")
    driver.implicitly_wait(10)
    clickeleById("审批管理")
    clickeleById("全部审批")
    driver.implicitly_wait(10)
    clickeleById("icon back left")
    clickeleById("icon back left")
    #回到首页
    time.sleep(10)
    driver.quit()




