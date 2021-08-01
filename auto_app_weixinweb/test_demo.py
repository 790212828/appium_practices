"""

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = '34d694360804'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['noReset'] = True  # 不要在会话前重置应用状态，默认：false，相当于保存缓存信息
        desired_caps['dontStopAppOnReset'] = True  # 不用重新打开app
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['appActivity'] = "com.tencent.wework.launch.LaunchSplashActivity"
        # 需要用到中文输入sendkeys("中文")，设置两个参数
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        #提高运行效率
        desired_caps['settings[waitForIdleTimeout]']=0

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    def test_demo(self):
        sleep(5)
        search_ele=self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/guu")
        search_ele.click()
        sleep(5)
        inputsearch_ele=self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fk1")
        inputsearch_ele.send_keys("吴一")
        sleep(5)
        #"new UiSelector().resourceId(\"com.tencent.wework:id/d2f\").childSelector(text(\"吴一\"))"
        # wuyi_ele=self.driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"com.tencent.wework:id/d2f\").childSelector(text(\"吴一\"))")
        wuyi_ele=self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tencent.wework:id/d2f").childSelector(text("吴一"))')
        wuyi_ele.click()
        sleep(5)
        # sendmess_ele=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.wework:id/dx1")')
        sendmess_ele=self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tencent.wework:id/dx1")')
        sendmess_ele.send_keys("测试")
        sleep(5)
        # sendclick_ele=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.wework:id/dwx")')
        sendclick_ele=self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tencent.wework:id/dwx")')
        sendclick_ele.click()

    def test_daka(self):
        # sleep(3)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()
        # sleep(3)
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().'
        #                                                 'resourceId("com.xueqiu.android:id/userName").text("ice_招行谷子地")'
        #                                                 '.instance(0));').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
                                                              'scrollable(true).instance(0)).'
                                                              'scrollIntoView(new UiSelector().text("打卡")'
                                                              '.instance(0));').click()

        # sleep(3)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tencent.wework:id/ghc").text("外出打卡")').click()
        # sleep(3)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tencent.wework:id/alv")').click()
        # sleep(3)
        result_txt=self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/mn").text
        expect_txt="外出打卡成功"
        assert result_txt==expect_txt

    #作业添加成员
    def test_add_member(self):
        """
        1、点击 通讯录按钮 进入通讯录页面
        2、滑动查找 添加成员 按钮，点击添加成员按钮进入页面
        3、点击 手动添加 按钮进入添加成员页面
        4、输入 姓名，输入手机号码
        5、选择 性别，使用显示等待定位点击“男性” 选项
        6、点击保存按钮
        7、返回到通行录页面，进行断言检查结果正确性
        :return:
        """
        sleep(3)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
                                                              'scrollable(true).instance(0)).'
                                                              'scrollIntoView(new UiSelector().text("添加成员")'
                                                              '.instance(0));').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/c7g").click()
        #姓名
        name_ele=self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../..//*[@resource-id="com.tencent.wework:id/au0"]')
        name_ele.send_keys("aa1")
        # phone_ele=self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机") and @resource-id="com.tencent.wework:id/au1"]/..//*[@resource-id="com.tencent.wework:id/eh0"]')
        phone_ele=self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机号")]')
        phone_ele.send_keys("18812341234")
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH,
        #                                                               "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']"))
        #点击性别选项按钮
        select_btn_ele=self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"性别")]/..//*[@resource-id="com.tencent.wework:id/av2"]')
        select_btn_ele.click()
        #显示等待，等待成功后点击
        WebDriverWait(self.driver,10).until(lambda x:x.find_element(MobileBy.XPATH,'//*[@text="女"]'))
        female_ele=self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]')
        female_ele.click()
        savebtn_ele=self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gur")
        try:
            savebtn_ele.click()
        except Exception as e:
            if savebtn_ele.get_attribute("enabled") == 'false':
                raise e
        #点击返回按钮，进行断言
        sleep(3)
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gu_").click()
        #滑动查找新增的成员名称
        expect_name="aa1"
        mem_name_ele=self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().'
                                                              'scrollable(true).instance(0)).'
                                                              'scrollIntoView(new UiSelector().text("aa1")'
                                                              '.instance(0));')
        assert mem_name_ele.text==expect_name












