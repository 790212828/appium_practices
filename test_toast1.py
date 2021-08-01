"""

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity
"""


from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '7.0'
        desired_caps['platformVersion'] = '6.0'
        # desired_caps['deviceName'] = '34d694360804'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['udid']='emulator-5554'
        # desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appPackage']='com.example.android.apis'
        # desired_caps['appActivity']="com.xueqiu.android.common.MainActivity"
        desired_caps['noReset'] = True  # 不要在会话前重置应用状态，默认：false
        # desired_caps['dontStopAppOnReset'] = True  # 不用重新打开app
        desired_caps['skipDeviceInitialization'] = True
        # desired_caps['appActivity'] = "io.appium.android.apis.view.PopupMenu1"
        #com.example.android.apis.view.PopupMenu1
        desired_caps['appActivity']="com.example.android.apis.view.PopupMenu1"
        #需要用到中文输入sendkeys("中文")，设置两个参数
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        # desired_caps['automationName']='uiautomator2'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_toast(self):
        sleep(10)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Make a Popup!').click()
        sleep(5)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='Search1']").click()
        print(self.driver.page_source)
        # print(self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'Click popup')]").text)