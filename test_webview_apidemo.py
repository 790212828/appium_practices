"""
查看相关的app包名：adb shell pm list package|findstr "browser"
查看浏览器版本信息：adb shell pm dump com.android.chrome |findstr "version"

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity

打开WEditor 可以用来定位
python -m weditor
"""
from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebViewApiDemo:


    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        # desired_caps['deviceName'] = '34d694360804'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        # desired_caps['appActivity']="com.xueqiu.android.common.MainActivity"
        desired_caps['noReset'] = True  # 不要在会话前重置应用状态，默认：false
        # desired_caps['dontStopAppOnReset'] = True  # 不用重新打开app
        # desired_caps['skipDeviceInitialization'] = True
        desired_caps['appActivity'] = "io.appium.android.apis.ApiDemos"
        #需要用到中文输入sendkeys("中文")，设置两个参数
        # desired_caps['unicodeKeyboard']=True
        # desired_caps['resetKeyboard']=True
        # desired_caps['automationName'] = 'uiautomator2'
        # desired_caps['settings[waitForIdleTimeout]'] = 0
        # desired_caps['chromedriverExecutable'] = r'E:\Softwork\Driver\appDriver\\'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_webview(self):
        sleep(5)
        self.driver.find_element_by_accessibility_id("Views").click()
        print(f"first : {self.driver.contexts}")
        webview='WebView'
        webview_ele=self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()'
                                                              '.scrollable(true).instance(0)).'
                                                              f'scrollIntoView(new UiSelector().text("{webview}").'
                                                              'instance(0))')
        sleep(3)
        webview_ele.click()
        sleep(5)
        context_list=self.driver.contexts
        print(f"第二个： {context_list}")

        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.context)
        a=self.driver.find_element(By.ID,"i_am_a_textbox")
        # a=self.driver.find_element(By.ID,'//*[@resource-id="i_am_a_textbox"]')
        a.send_keys("this is a test string")
        # b=self.driver.find_element(By.ID,'//*[@resource-id="i_am_a_textbox"]')

        #//*[@resource-id="i am a link"]
        sleep(15)
        self.driver.find_element(By.XPATH,'//*[@id="i am a link"]').click()
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"i am a link").click()
        print(self.driver.page_source)




