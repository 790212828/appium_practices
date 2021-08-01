import yaml
from appium import webdriver

from test_appium.data_driven2.pages.base_page import BasePage
from test_appium.data_driven2.pages.main import Main


class App(BasePage):
    _package="com.xueqiu.android"
    _activity="com.xueqiu.android.view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:
            caps={}
            caps['platformName']='android'
            caps['platformVersion']='6.0'
            caps['deviceName']=yaml.safe_load(open('../pages/configuration.yaml'))['caps']['udid']
            caps['udid']='emulator-5554'
            caps['appPackage']=self._package
            caps['appActivity']=self._activity
            caps['noSign']=True#不用重新安装appium相关apk
            caps['noReset']=True#在当前session前不重置app状态
            # caps['dontStopAppOnReset'] = True  # 不用重新打开app
            caps['skipDeviceInitialization'] = True
            # 需要用到中文输入sendkeys("中文")，设置两个参数
            caps['unicodeKeyboard'] = True
            caps['resetKeyboard'] = True
            # desired_caps['automationName'] = 'uiautomator2'
            caps['settings[waitForIdleTimeout]'] = 0
            # caps['avd'] = '60012'
            # caps['chromedriverExecutable'] = r'E:\Softwork\Driver\appDriver\\'

            self._driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)

        else:
            self._driver.start_activity(self._package,self._activity)

        self._driver.implicitly_wait(5)

        return self

    def main(self)->Main():
        return Main(self._driver)

    def stop(self):
        # self.logger.debug("停止，退出APP")
        self._driver.quit()



