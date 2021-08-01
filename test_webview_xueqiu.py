"""
查看相关的app包名：adb shell pm list package|findstr "browser"
查看浏览器版本信息：adb shell pm dump com.android.chrome |findstr "version"

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity

打开WEditor 可以用来定位
python -m weditor


查询包中chromedriver的版本信息：adb shell pm dump com.xueqiu.android |findstr "version"


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
        desired_caps['deviceName'] = '34d694360804'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity']="com.xueqiu.android.view.WelcomeActivityAlias"
        desired_caps['noReset'] = True  # 不要在会话前重置应用状态，默认：false
        desired_caps['dontStopAppOnReset'] = True  # 不用重新打开app
        desired_caps['skipDeviceInitialization'] = True
        #需要用到中文输入sendkeys("中文")，设置两个参数
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['settings[waitForIdleTimeout]'] = 0
        # desired_caps['chromedriverExecutable'] = r'E:\Softwork\Driver\appDriver\\'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_webview_xueqiu(self):
        #点击交易
        sleep(5)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="交易"]').click()
        print(f"打印当前的页面是否是原生的还是webview:{self.driver.contexts}")
        #点击平安证券进行开户操作
        # print(f"查看window_handles：{self.driver.window_handles}")
        # print(f"查看查看实际窗口：{self.driver.current_window_handle}")
        click_locator=(MobileBy.XPATH,'//*[@text="平安证券"]')

        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(click_locator))
        self.driver.find_element(*click_locator).click()
        #切换webview的窗口
        # kaihu_window=self.driver.window_handles[-1]
        # self.driver.switch_to.window(kaihu_window)

        # 切换上下文
        # self.driver.switch_to.context(self.driver.contexts[-1])
        print(f"打印当前的页面是否是原生的还是webview:{self.driver.contexts}")
        # search_locator = (By.ID, "index-bn")
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        #输入用户名、验证码，点击立即开户按钮
        sleep(5)
        phone_num_locator=(MobileBy.XPATH,'//*[@resource-id="phone-number"]')
        WebDriverWait(self.driver,60).until(expected_conditions.visibility_of_element_located(phone_num_locator))
        self.driver.find_element(*phone_num_locator).send_keys("13612341234")

        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="code"]').send_keys("1234")
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='立即开户']").click()
        self.driver.find_element(MobileBy.CSS_SELECTOR,".btn-submit").click()






