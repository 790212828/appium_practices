"""

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity
"""
from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:


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
        pass

    def test_wait(self):
        sleep(3)
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        sleep(3)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        # sleep(3)
        locator=(MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable(locator))
        WebDriverWait(self.driver,10).until(lambda x:x.find_element(*locator))
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']"))
        current_price = self.driver.find_element(*locator).text
        result = int(float(current_price))
        print(f"打印当前09988 对应的股票价格是：{current_price},type:{type(result)}")
        print(result)
        expect_price=200
        # assert result >expect_price
        assert_that(result,close_to(expect_price,expect_price*0.1))

        sleep(10)