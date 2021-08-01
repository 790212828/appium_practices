"""

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity
"""


from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestDW:
    username='13612919781'
    pwd='a12345678'

    # @pytest.mark.skip
    def setup_890(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = '34d694360804'
        desired_caps['appPackage'] = 'com.xueqiu.android'
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

    # @pytest.mark.skip
    def test_get_attr(self):
        sleep(5)
        search_ele=self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(f"content-desc:{search_ele.get_attribute('content-desc')}")
        print(f"resource-id:{search_ele.get_attribute('resource-id')}")
        print(f"enable:{search_ele.get_attribute('enabled')}")
        print(f"checkable:{search_ele.get_attribute('checkable')}")
        print(f"clickable:{search_ele.get_attribute('clickable')}")
        print(f"bounds:{search_ele.get_attribute('bounds')}")
        assert 'search' in search_ele.get_attribute("resource-id")

    def test_assert(self):
        a=10
        b=20
        assert a>b
        assert 'h' in 'this'

    def test_hamcrest(self):
        # assert_that(10,equal_to(9))
        assert_that(8,close_to(10,2))#close_to 是10上下浮动+或者-2
        assert_that('contains some string',contains_string('string'))#包含字符串的用法












