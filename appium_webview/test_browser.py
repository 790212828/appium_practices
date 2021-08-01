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
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        des_caps={}
        des_caps['platformName']='Android'
        des_caps['platformVersion']='7.0'
        des_caps['deviceName']='34d694360804'
        des_caps['noReset']=True
        # des_caps['noSign']=True
        des_caps['browserName']='Chrome'
        des_caps['automationName']='uiautomator2'
        des_caps['settings[waitForIdleTimeout]']=0
        des_caps['chromedriverExecutable']=r'E:\Softwork\Driver\appDriver\chromedriver.exe'
        # des_caps['skipDeviceInitialization'] = True
        # des_caps['chromeOptions']={'androidProcess': 'com.android.chrome'}


        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass


    def test_browser(self):


        self.driver.get("http://m.baidu.com")

        sleep(5)
        self.driver.find_element(By.ID,"index-kw").click()
        self.driver.find_element(By.ID,"index-kw").send_keys("appium")
        search_locator=(By.ID,"index-bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()




