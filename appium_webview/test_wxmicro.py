"""
查看相关的app包名：adb shell pm list package|findstr "browser"
查看浏览器版本信息：adb shell pm dump com.android.chrome |findstr "version"

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity

打开WEditor 可以用来定位
python -m weditor


查询包中chromedriver的版本信息：adb shell pm dump com.xueqiu.android |findstr "version"


"""

from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWXMicro:

    # 为了演示方便，未使用page object模式
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps['platformVersion']="7.0"
        caps["deviceName"] = "34d694360804"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
        caps["noReset"] = True
        caps['noSign']=True
        caps['dontStopAppOnReset']=True# 不用重新打开app
        caps['skipDeviceInitialization'] = True#Appium启动时跳过初始化设置
        caps['unicodeKeyboard'] = True#需要用到中文输入sendkeys("中文")，设置两个参数
        caps['resetKeyboard'] = True#需要用到中文输入sendkeys("中文")，设置两个参数
        caps['automationName'] = 'uiautomator2'
        caps['settings[waitForIdleTimeout]'] = 0#优化超时时间

        caps['chromedriverExecutable'] = \
            'E:/Softwork\Driver/appDriver/chromedriver_77.0.3865.120.exe'

        # options = ChromeOptions()
        # options.add_experimental_option('androidProcess', 'com.tencent.mm:appbrand0')
        caps['chromeOptions'] = {'androidProcess':'com.tencent.mm:appbrand0'}

        caps['adbPort'] = 5038

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(10)

        self.enter_micro_program()
        print(self.driver.contexts)

    def enter_micro_program(self):
        # 原生自动化测试
        size = self.driver.get_window_size()
        #获取手机屏幕大小，屏幕中间向下滑动
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.9)
        # self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
        self.driver.find_element(By.ID,"com.tencent.mm:id/nr").click()#点击搜索框
        self.driver.find_element(By.XPATH, "//*[@text='取消']")
        self.driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys("雪球")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        self.driver.find_element(By.XPATH, "//*[@text='自选']")

    def find_top_window(self):
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print(self.driver.title)
            else:
                self.driver.switch_to.window(window)

    def test_search_webview(self):
        # 进入webview
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.implicitly_wait(10)
        self.find_top_window()

        # css定位
        self.driver.find_element(By.CSS_SELECTOR, "[src*=stock_add]").click()
        # 等待新窗口
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, "._input").click()
        # 输入
        self.driver.switch_to.context("NATIVE_APP")
        ActionChains(self.driver).send_keys("alibaba").perform()
        # 点击
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item")
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item").click()