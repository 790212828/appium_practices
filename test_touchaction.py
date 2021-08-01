
"""

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = '34d694360804'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        # desired_caps['appActivity']="com.xueqiu.android.common.MainActivity"
        desired_caps['noReset'] = True  # 不要在会话前重置应用状态，默认：false
        # desired_caps['dontStopAppOnReset'] = True  # 不用重新打开app
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['appActivity'] = "com.samsung.ui.FlashActivity"
        # 需要用到中文输入sendkeys("中文")，设置两个参数
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_touchaction_unlock(self):
        sleep(3)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("cn.kmob.screenfingermovelock:id/topLayout").click()
        sleep(5)
        action=TouchAction(self.driver)
        action.press(x=185,y=290).wait(200).move_to(x=540,y=290).wait(200).move_to(x=900,y=290).wait(200)\
            .move_to(x=900,y=650).wait(200)\
            .move_to(x=900,y=1000).wait(100)\
            .release().perform()





















