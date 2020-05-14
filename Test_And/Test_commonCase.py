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
    for i in range(number):
        loc = ("xpath", "//*[@text='始终允许']")
        try:
            e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
            e.click()
            time.sleep(3)
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
    y1 = get_size()[1] * 0.75
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
    TouchAction(driver).press(ele).wait(time).move_to(x=a * X, y=b2 * Y).release().perform()


def browsehouses(count):
    '''
    按房源列表顺序浏览房源
    :param count: 浏览次数
    :return:
    '''
    for i in range(count):
        driver.implicitly_wait(10)
        houses = driver.find_elements_by_xpath("//*[@resource-id='com.fooww.soft.android.Presentation:id/rv_house_list']/android.widget.LinearLayout")
        houses[i].click()
        time.sleep(1)
        swipe_up(1)
        time.sleep(2)
        driver.keyevent(4)

def switchtabs(count):
    for i in range(1,count):
        driver.implicitly_wait(10)
        tabs = driver.find_elements_by_xpath("//*[@resource-id='android:id/tabs']/android.widget.LinearLayout")
        tabs[i].click()
        time.sleep(10)



if __name__ == "__main__":
    # 处理4个权限弹窗
    always_allow(driver, 4)
    # 点击【跳过】
    driver.implicitly_wait(20)
    clickeleById("com.fooww.soft.android.Presentation:id/btn_splash_skip")
    driver.implicitly_wait(10)
    time.sleep(3)
    # 输入用户名和密码
    sendkeyseleById("com.fooww.soft.android.Presentation:id/etEmail", "15900000001")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/etPassword", "1234567:pUblic")
    clickeleById("com.fooww.soft.android.Presentation:id/btnLogin")
    driver.implicitly_wait(5)
    # 处理1个权限弹窗
    always_allow(driver, 1)

    ##个人房源常见操作
    # 点击【发现】tab
    driver.implicitly_wait(10)
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
    time.sleep(10)
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
    time.sleep(10)
    # 返回
    driver.keyevent(4)
    driver.keyevent(4)
    # 点击【房源】
    clickeleById("com.fooww.soft.android.Presentation:id/house_badge")
    # 点击房源列表第一套房源（刚刚导入）
    driver.implicitly_wait(10)
    houses = driver.find_elements_by_xpath(
        "//*[@resource-id='com.fooww.soft.android.Presentation:id/rv_house_list']/android.widget.LinearLayout")
    houses[0].click()
    # 下滑
    time.sleep(10)
    swipe_up(1)
    time.sleep(10)
    driver.keyevent(4)

    ##房源常见操作
    # 浏览第1-6套房源
    browsehouses(6)
    driver.implicitly_wait(10)
    # 点击【+】
    clickeleById("com.fooww.soft.android.Presentation:id/main_floating_action_bar")
    # 点击【录入房源】
    clickeleByXpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View[1]")
    # 点击【小区】
    clickeleById("com.fooww.soft.android.Presentation:id/tv_house_add_row_select_value")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/mEtSearch", "闸北")
    driver.implicitly_wait(10)
    # 搜索小区
    clickeleByXpath("//*[@text='闸北公房']")
    driver.implicitly_wait(10)
    # 填写总价
    sendkeyseleByXpath("//*[@text='请填写']", "500")
    sendkeyseleByXpath("//*[@text='请填写']", "80")
    time.sleep(10)
    # 选择朝向
    clickeleByXpath("//*[@text='其他']")
    driver.implicitly_wait(2)
    clickeleByXpath("//*[@text='东西']")
    clickeleByXpath("//*[@text='确定']")
    time.sleep(10)
    # 选择装修
    clickeleByXpath("//*[@text='毛坯']")
    driver.implicitly_wait(2)
    clickeleByXpath("//*[@text='精装']")
    clickeleByXpath("//*[@text='确定']")
    # 向上滑动
    time.sleep(10)
    swipe_up(2)
    driver.implicitly_wait(5)
    # 点击照片
    clickeleById("com.fooww.soft.android.Presentation:id/row_add_edit_house_take_photo")
    driver.implicitly_wait(2)
    clickeleByXpath("//*[@text='本地图片']")
    # 处理照片访问权限
    driver.implicitly_wait(5)
    always_allow(driver, 1)
    # 选择并上传图片
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/check_view")
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='使用1']")
    time.sleep(10)
    # 返回
    driver.keyevent(4)
    driver.implicitly_wait(10)
    # 点击【保存】
    clickeleByXpath("//*[@text='保存']")
    # 查看房源详情
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='闸北公房']")
    # 查看业主信息
    clickeleById("com.fooww.soft.android.Presentation:id/ivOwner")
    driver.implicitly_wait(5)
    # 返回房源详情
    driver.keyevent(4)
    driver.implicitly_wait(5)
    # 返回房源列表
    driver.keyevent(4)
    # 删除房源
    driver.implicitly_wait(10)
    TouchAction(driver).long_press(geteleByXpath("//*[@text='闸北公房']")).perform()
    clickeleByXpath("//*[@text='删除']")
    clickeleById("com.fooww.soft.android.Presentation:id/md_buttonDefaultPositive")
    # 搜索房源
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/et_search_bar")
    driver.implicitly_wait(10)
    sendkeyseleById("com.fooww.soft.android.Presentation:id/mEtKeyword", "广场")
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='搜索")
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='清空全部搜索/筛选条件']")

    ##客源常见操作
    # 点击【客源】tab
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/demand_badge")
    driver.implicitly_wait(10)
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
    time.sleep(10)
    # 向下滑动
    swipe_up(1)
    # 填写户型
    driver.implicitly_wait(10)
    sendkeyseleById("com.fooww.soft.android.Presentation:id/et_demand_room_count", "2")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/et_demand_hall_count", "1")
    # 选择区县
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/tv_demand_district_edit")
    driver.implicitly_wait(5)
    clickeleByXpath("//*[@text='闸北']")
    time.sleep(10)
    # 添加意向小区
    clickeleById("com.fooww.soft.android.Presentation:id/tv_demand_add_intention_community")
    sendkeyseleById("com.fooww.soft.android.Presentation:id/mEtSearch", "测试闸北")
    driver.implicitly_wait(5)
    clickeleById("com.fooww.soft.android.Presentation:id/tvCommunity")
    # 保存
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='保存']")
    # 查看客源详情
    driver.implicitly_wait(5)
    clickeleByXpath("//*[@text='测试顾客And']")
    driver.implicitly_wait(5)
    # 查看客源电话
    clickeleById("com.fooww.soft.android.Presentation:id/iv_call_phone")
    # 匹配房源（选第一套）
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/iv_demand_match_house")
    clickeleByXpath("//*[@text='按需求信息匹配']")
    driver.implicitly_wait(10)
    houses = driver.find_elements_by_xpath(
        "//*[@resource-id='com.fooww.soft.android.Presentation:id/rv_house_list']/android.widget.LinearLayout")
    houses[0].click()
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='添加意向']")
    time.sleep(10)
    driver.keyevent(4)
    driver.keyevent(4)
    # 添加带看
    driver.implicitly_wait(5)
    clickeleById("com.fooww.soft.android.Presentation:id/iv_add_visit_record")
    clickeleByXpath("//*[@text='添加']")
    # 添加带看房源
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/et_customer")
    houses = driver.find_elements_by_xpath(
        "//*[@resource-id='com.fooww.soft.android.Presentation:id/rv_house_list']/android.widget.LinearLayout")
    houses[0].click()
    time.sleep(10)
    clickeleById("com.fooww.soft.android.Presentation:id/md_buttonDefaultPositive")
    time.sleep(10)
    sendkeyseleById("com.fooww.soft.android.Presentation:id/et_description","添加房源情况…添加房源情况")
    clickeleByXpath("//*[@text='确定']")
    time.sleep(10)
    # 返回
    driver.keyevent(4)
    # 返回
    driver.keyevent(4)
    # 删除客源
    driver.implicitly_wait(10)
    TouchAction(driver).long_press(geteleByXpath("//*[@text='测试顾客And']")).perform()
    clickeleByXpath("//*[@text='删除']")
    clickeleById("com.fooww.soft.android.Presentation:id/md_buttonDefaultPositive")
    # 查询
    driver.implicitly_wait(5)
    clickeleById("com.fooww.soft.android.Presentation:id/iv_title_bar_filter")
    driver.implicitly_wait(5)
    clickeleById("com.fooww.soft.android.Presentation:id/etUserOwner")
    clickeleByXpath("//*[@text='尼克斯1115']")
    driver.implicitly_wait(5)
    clickeleById("com.fooww.soft.android.Presentation:id/etBusinessState")
    clickeleByXpath("//*[@text='状态不限']")
    clickeleById("com.fooww.soft.android.Presentation:id/btnConfirmCondition")

    ##消息常见操作
    # 点击【消息】tab
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/message_badge")
    driver.implicitly_wait(10)
    # 点击【系统消息】
    clickeleByXpath("//*[@text='系统消息']")
    time.sleep(10)
    driver.keyevent(4)
    time.sleep(10)
    # 点击【微站用户】
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='微站客户']")
    # 点击【访客动态】
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/customer_dynm")
    # 向下滑动
    time.sleep(10)
    swipe_up(2)
    # 点击【分享获客】
    time.sleep(10)
    clickeleById("com.fooww.soft.android.Presentation:id/customer_share")
    # 点击【立即分享】
    time.sleep(10)
    clickeleById("com.fooww.soft.android.Presentation:id/sg_submit")
    # 下拉分享
    time.sleep(10)
    drag(driver, geteleByXpath("//*[@text='租房']"), 500)
    # 退出介绍页
    driver.keyevent(4)
    # 再次下拉分享
    time.sleep(10)
    drag(driver, geteleByXpath("//*[@text='租房']"), 500)
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/mBtCollect")
    # 点击【分享】
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='分享']")
    # 选择【微信】
    time.sleep(10)
    clickeleByXpath("//*[@text='微信好友']")
    # 选择微信要分享的人
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='Cady']")
    # 点击【发送】
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='分享']")
    # 点击【返回手机梵讯】
    clickeleByXpath("//*[@text='返回手机梵讯']")
    # 返回
    driver.keyevent(4)
    # 返回
    driver.keyevent(4)

    ##个人tab常见操作
    #点击【我的】
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/mine_badge")
    time.sleep(10)
    swipe_up(1)
    driver.implicitly_wait(10)
    #点击【海报中心】
    clickeleByXpath("//*[@text='海报中心']")
    #切换tab
    clickeleByXpath("//*[@text='喜报']")
    time.sleep(10)
    clickeleByXpath("//*[@text='拓客']")
    time.sleep(10)
    clickeleByXpath("//*[@text='节日']")
    time.sleep(10)
    clickeleByXpath("//*[@text='招聘']")
    time.sleep(10)
    #返回
    driver.keyevent(4)
    #点击【合同】
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='合同']")
    time.sleep(10)
    #返回
    driver.keyevent(4)
    #点击【收藏】
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='收藏']")
    time.sleep(10)
    driver.keyevent(4)
    #点击【考勤】
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='考勤']")
    #切换tabs
    switchtabs(4)
    #返回
    driver.keyevent(4)
    #点击【审批管理】
    driver.implicitly_wait(10)
    clickeleByXpath("//*[@text='审批管理']")
    #点击【全部审批】
    driver.implicitly_wait(10)
    clickeleById("com.fooww.soft.android.Presentation:id/mRlApprovalAll")
    time.sleep(10)
    driver.keyevent(4)
    driver.keyevent(4)
    #回到首页
    time.sleep(10)
    driver.quit()
