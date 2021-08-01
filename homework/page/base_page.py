"""
查看相关的app包名：adb shell pm list package|findstr "browser"
查看浏览器版本信息：adb shell pm dump com.android.chrome |findstr "version"

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity

打开WEditor 可以用来定位
python -m weditor


查询包中chromedriver的版本信息：adb shell pm dump com.xueqiu.android |findstr "version"
"""

#基类，完成底层封装，比如常用的一些方法，初始化driver 如：find_element方法,click,send,step查询步骤

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

# import logging

from test_appium.homework.log.app_logger import AppLogger



class BasePage():
    logger = AppLogger().get_logger()
    # logging.basicConfig(level=logging.INFO)
    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    #封装find_element方法
    def find(self,by,value):
        # logging.info(f"定位方式：{by}，定位内容：{value}")
        self.logger.info(f"定位方式：{by}，定位内容：{value}")
        return self._driver.find_element(by,value)


    def impactivity_sleep(self,num):
        # logging.info(f"本次隐式等待时间：{num} 秒")
        self.logger.info(f"本次隐式等待时间：{num} 秒")
        self._driver.implicitly_wait(num)

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

    def assert_text(self,expect_txt,actual_txt):
        # logging.info(f"判断实际结果{actual_txt} 是否等于== 预期结果{expect_txt}")
        self.logger.info(f"判断实际结果{actual_txt} 是否等于== 预期结果{expect_txt}")
        assert actual_txt==expect_txt