"""
查看相关的app包名：adb shell pm list package|findstr "browser"
查看浏览器版本信息：adb shell pm dump com.android.chrome |findstr "version"

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity

打开WEditor 可以用来定位
python -m weditor


查询包中chromedriver的版本信息：adb shell pm dump com.xueqiu.android |findstr "version"

查看avdy已创建模拟器列表 emulator -list-avds
启动Android模拟器 emulator -avd [模拟器列表名]

"""
#app.py 启动、重启、停止、关闭
import logging

from appium import webdriver

from test_appium.homework.page.base_page import BasePage
from test_appium.homework.page.index_page import IndexPage


class App(BasePage):
    _package="com.tencent.wework"
    _activity="com.tencent.wework.launch.LaunchSplashActivity"
    def start(self):
        if self._driver==None:
            # logging.info("driver == None,初始化driver")
            self.logger.info("driver == None,初始化driver")
            print("driver == None")
            caps = {}
            caps["platformName"] = 'Android'
            caps['platformVersion'] = '7.0'
            caps['deviceName'] = '34d694360804'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            caps['autoGrantPermissions'] = True
            caps['automationName'] = 'uiautomator2'
            # 防止清空缓存信息，不要在会话前重置应用状态，默认：false，相当于保存缓存信息
            caps['noReset'] = True
            # caps['dontStopAppOnReset'] = True  # 不用重新打开app
            caps['skipDeviceInitialization'] = True
            # # 需要用到中文输入sendkeys("中文")，设置两个参数
            caps['unicodeKeyboard'] = True
            caps['resetKeyboard'] = True
            # 提高运行效率
            caps['settings[waitForIdleTimeout]'] = 0

            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self._driver.implicitly_wait(10)
        else:
            print("复用Driver ")
            self.logger.debug("已初始化过Driver,现在复用Driver")
            self.restart()


        return self#当在主代码中调用app类中的start方法后还想调用app类中其他方法就需要 调用完方法后return self

    def restart(self):
        self.logger.debug("重新启动APP")
        self._driver.close_app()
        self._driver.launch_app()
        return  self

    def stop(self):
        self.logger.debug("停止，退出APP")
        self._driver.quit()

    def close(self):
        pass

    def goto_main(self):
        #页面入口方法
        self.logger.debug("页面入口方法")
        return IndexPage(self._driver)
