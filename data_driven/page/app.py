from appium import webdriver

from test_appium.data_driven.page.base_page import BasePage
from test_appium.data_driven.page.main import Main


class App(BasePage):
    _package='com.xueqiu.android'
    _activity="com.xueqiu.android.view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:
            caps={}
            caps["platformName"]='Android'
            caps['platformVersion'] = '7.0'
            caps['deviceName'] = '34d694360804'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            caps['autoGrantPermissions']=True
            caps['automationName']='uiautomator2'
            # caps['noReset'] = True  # 不要在会话前重置应用状态，默认：false，相当于保存缓存信息
            # caps['dontStopAppOnReset'] = True  # 不用重新打开app
            # caps['skipDeviceInitialization'] = True
            # # 需要用到中文输入sendkeys("中文")，设置两个参数
            # caps['unicodeKeyboard'] = True
            # caps['resetKeyboard'] = True
            # 提高运行效率
            caps['settings[waitForIdleTimeout]'] = 0

            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(self._package,self._activity)
        return  self

    def main(self):
        return Main(self._driver)