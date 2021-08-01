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

#app包含了 appium 初始化操作,这个操作在各个业务线都能复用，所以app的代码可以时框架的一部分
# app.py 启动，重启，关闭，停止
from appium import webdriver

# from test_appium.pages.base_page import BasePage
# from test_appium.pages.index_page import IndexPage
# from test_appium.test_ui_framework.pages.base_page import BasePage
# from test_appium.test_ui_framework.pages.index_page import IndexPage
from test_appium.test_ui_framework.ui_framework.base_page import BasePage
from test_appium.test_ui_framework.ui_framework.page.index_page import IndexPage


class App(BasePage):
    _package = "com.tencent.wework"
    _activity = "com.tencent.wework.launch.LaunchSplashActivity"
    _xueqiu_package='com.xueqiu.android'
    _xueqiu_activity='com.xueqiu.android.view.WelcomeActivityAlias'

    def start(self):
        if self._driver == None:
            print("driver == None, 创建driver")
            # caps = {}
            # caps["platformName"] = "Android"
            # caps["deviceName"] = "hogwarts"
            # # Mac/Linux: adb logcat |grep -i activitymanager (-i忽略大小写)
            # # Windows:  adb logcat |findstr /i activitymanager
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.LaunchSplashActivity"
            # # 防止清空缓存-比如登录信息
            # caps["noReset"] = "true"
            caps = {}
            caps["platformName"] = 'Android'
            caps['platformVersion'] = '7.0'
            caps['deviceName'] = '34d694360804'
            caps['appPackage'] = self._xueqiu_package
            caps['appActivity'] = self._xueqiu_activity
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

            # 最重要的一步，与server 建立连接
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待 5 秒
            self._driver.implicitly_wait(5)
        else:
            print("复用driver")
            self.restart()
        return self

    def restart(self):
        self._driver.close_app()
        self._driver.launch_app()

    def stop(self):
        self._driver.quit()

    def goto_main(self):
        # 页面的入口方法
        return IndexPage(self._driver)