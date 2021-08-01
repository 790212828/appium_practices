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


    def setup_class(self):
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
        # self.driver.back()
        # pass
        sleep(1)
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()

    @pytest.mark.parametrize('searchkey,searchname,search_type,price',[
        ['alibaba','阿里巴巴','BABA',200.00],
        ('xiaomi','小米集团-W','01810',28.00)
    ])
    def test_search(self,searchkey,searchname,search_type,price):
        """
        1、打开 雪球应用
        2、点击 搜索框
        3、输入 搜索词 ‘allbaba’ or 'xiaomi'
        4、点击第一个搜索结果
        5、判断 股票价格
        :return:
        """
        sleep(5)
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
        sleep(3)
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        sleep(5)
        print(f"searchname:{searchname},type:{type(searchname)}")
        print(f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{searchname}']")
        self.driver.find_element(MobileBy.XPATH,f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{searchname}']").click()
        sleep(3)
        price_ele=self.driver.find_element(MobileBy.XPATH,f'//*[@text="{search_type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        current_price=float(price_ele.get_attribute("text"))
        expect_price=price
        assert_that(current_price,close_to(expect_price,expect_price*0.1))















