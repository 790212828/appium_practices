
"""

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity
"""
from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
    username='13612919781'
    pwd='a12345678'

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = '34d694360804'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity']="com.xueqiu.android.common.MainActivity"
        desired_caps['noReset'] = True  # 不要在会话前重置应用状态，默认：false
        desired_caps['dontStopAppOnReset'] = True  # 不用重新打开app
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['appActivity'] = "com.xueqiu.android.view.WelcomeActivityAlias"
        #需要用到中文输入sendkeys("中文")，设置两个参数
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        1、打开 雪球app
        2、点击搜索输入框
        3、向搜索输入框输入 “阿里巴巴”
        4、在搜索结果里面选择 “阿里巴巴”，然后进行点击
        5、获取这只上香港 阿里巴巴的报价，并判断 这只股价的价格>200
        
        """
        sleep(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        sleep(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()

    def test_attr(self):
        """
        1、打开雪球app
        2、定位首页的搜索框
        3、判断搜索框的是否可用，并查看搜索框的name值
        4、打印搜索框这个元素的左上角坐标和它的高度
        5、向搜索框输入：alibaba
        6、判断【阿里巴巴】是否可见
        7、如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
        :return:
        """
        sleep(5)
        self.driver.implicitly_wait(5)
        search_ele=self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enable=search_ele.is_enabled()
        print(f"search_enable:{search_enable}")
        print(f"search_ele.text:{search_ele.text}")
        print(f"元素的长宽高：{search_ele.location}")
        print(f"{search_ele.size}")
        if search_enable==True:
            search_ele.click()
            sleep(3)
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            self.driver.implicitly_wait(5)
            alibaba_ele=self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']")
            # alibaba_isdisplay=alibaba_ele.is_displayed()
            alibaba_isdisplay=alibaba_ele.get_attribute("displayed")
            print(f"display：{alibaba_isdisplay}")
            if alibaba_isdisplay=='true':
                print("搜索成功")
                alibaba_ele.click()
            else:
                print("搜索失败")
    def test_touchaction(self):
        action=TouchAction(self.driver)
        print(self.driver.get_window_rect())
        windows_rect=self.driver.get_window_rect()
        width=windows_rect['width']
        height=windows_rect['height']
        x_start=width/2
        y_start=height*0.8
        y_end=height*0.2
        action.press(x=x_start,y=y_start).wait(300).move_to(x=x_start,y=y_end).release().perform()

    def test_get_current(self):
        sleep(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        sleep(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()

        current_price=self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        result = int(float(current_price))
        print(f"打印当前09988 对应的股票价格是：{current_price},type:{type(result)}")
        print(result)
        assert  result > 200
        sleep(10)
    def test_myinfo(self):
        """
        1、点击我的，进入到个人信息页面
        2、点击登录，进入登录页面
        3、输入用户名，输入密码
        4、点击登录
        :return:
        """
        sleep(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        sleep(5)
        # self.driver.find_element_by_xpath("//*[@text='帐号密码登录']").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        sleep(5)
        # self.driver.find_element_by_id("com.xueqiu.android:id/login_account").send_keys(self.username)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys(self.username)
        self.driver.implicitly_wait(5)
        # self.driver.find_element_by_id("com.xueqiu.android:id/login_password").send_keys(self.pwd)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys(self.pwd)
        self.driver.implicitly_wait(5)
        # self.driver.find_element_by_id("com.xueqiu.android:id/button_next").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("雪球")').click()
        sleep(3)
        #new UiSelector().resourceId("com.xueqiu.android:id/home_search").childSelector(resourceId("com.xueqiu.android:id/tv_search"))
        #new UiSelector().resourceId("com.xueqiu.android:id/home_search").childSelector(textContains("搜索股票/组合/用户/讨论"))
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/home_search").childSelector(resourceId("com.xueqiu.android:id/tv_search"))').click()
        sleep(5)
        # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/search_input_text")').send_keys("阿里巴巴")
        sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()

        sleep(20)

    def test_scroll_find_element(self):
        sleep(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_text").fromParent(text("关注的人"))').click()
        # sleep(3)
        self.wait=WebDriverWait(self.driver,50)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        'resourceId("com.xueqiu.android:id/userName").text("ice_招行谷子地")'
                                                        '.instance(0));').click()

        sleep(10)


if __name__ == '__main__':
    pytest.main()



