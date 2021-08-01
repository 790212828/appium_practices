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
from time import sleep

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    _driver:WebDriver
    _back_list=[(By.ID,'iv_close')]
    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    def find(self,locator,value):
        sleep(3)
        try:
            element= self._driver.find_element(locator,value)
            return element
        except:
            for black in self._back_list:
                sleep(3)
                elements=self._driver.find_elements(*black)
                if len(elements)>0:
                    elements[0].click()
                    break
            #处理完黑名单后，再次查询是否还有黑名单，如果没有则再次查找原来的元素
            return self.find(locator,value)




    def click(self,locator,value):
        self._driver.find_element(locator,value).click()

    def swipe_find(self,text,num=4):
        # logging.info(f"滑动查找，定位内容：{text}，滑动次数：{num}")
        self.logger.info(f"滑动查找，定位内容：{text}，滑动次数：{num}")

        # num=3
        for i in range(0,num):
            if i==num-1:
                raise NoSuchElementException(f"找了{num}次，没有找到元素")
            try:
                if i==num-1:
                    # logging.info(f"滑动{num-1}次后查找元素")
                    self.logger.info(f"滑动{num-1}次后查找元素")
                    self.impactivity_sleep(10)
                    return self.find(MobileBy.XPATH,f"//*[@text='{text}']")

                else:
                    # logging.info(f"滑动{i}次后查找元素")
                    self.logger.info(f"滑动{i}次后查找元素")
                    return self.find(MobileBy.XPATH, f"//*[@text='{text}']")
            except:
                self.logger.error("Error 没有查询到元素")
                size=self._driver.get_window_size()
                width=size['width']
                height=size['height']

                # print("Error 未找到元素，滑动")
                # logging.debug(f"手机屏幕 宽：{width},长：{height}")
                # logging.info(f"Error 未找到元素，滑动第{i+1}次")

                self.logger.debug(f"手机屏幕 宽：{width},长：{height}")
                self.logger.info(f"Error 未找到元素，滑动第{i+1}次")

                startx=width/2
                starty=height*0.8
                endx=startx
                endy=height*0.2
                duration=2000#单位为毫秒计算，2000=2秒

                # logging.debug(f"滑动 初始值x：{startx}， 初始值 y：{starty}")
                # logging.debug(f"滑动后 x：{endx}，y：{endy}，滑动动画时间：{float(duration / 1000)}秒")

                self.logger.debug(f"滑动 初始值x：{startx}， 初始值 y：{starty}")
                self.logger.debug(f"滑动后 x：{endx}，y：{endy}，滑动动画时间：{float(duration/1000)}秒")

                self._driver.swipe(startx,starty,endx,endy,duration)

    def steps(self,path):
        with open(path) as f:
            steps=yaml.load(f)
        element=None
        for step in steps:
            # loactor: tv_search
            # action: click
            if "by" in step.keys():
                element=self.find(step['by'],step['loactor'])
            if "action" in step.keys():
                action=step['action']
                if action=="click":
                    element.click()
