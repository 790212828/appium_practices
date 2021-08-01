

# 基类， 完成底层封装，比如常用的一些方法，初始化 driver，find。。。。
#基类实现底层封装，它也可以被复用，所以basepage也应该属于框架层
from time import sleep

import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

root = logging.getLogger()
print(root.handlers)
for h in root.handlers[:]:
    root.removeHandler(h)


class BasePage:
    _driver: WebDriver
    _back_list = [(By.ID, 'iv_close')]
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self._driver = driver


    #如果添加的功能越来越多，find方法会无限增长
    #如果find方法代码增加非常多的话，会很难维护
    #解决：可以利用装饰器进行增强find方法，把黑名单放到黑名单中增强find方法
    # aa=yaml.safe_load(open('黑名单.yaml'))
    # @pytest.mark.parametrize("by,value",aa['by'],aa['value'])

    def find(self, by, value):
        logging.info(by)
        logging.info(value)
        #黑名单处理逻辑
        sleep(3)
        try:
            # WebDriverWait(self,10).until()
            # element = self._driver.find_element(by, value)
            element=WebDriverWait(self._driver,10).until(lambda x:x.find_element(by, value))
            return element
        except:
            for black in self._back_list:
                sleep(3)
                elements = self._driver.find_elements(*black)
                # elements=WebDriverWait(self._driver,10).until(lambda x:x.find_elements(*black))
                if len(elements) > 0:
                    elements[0].click()
                    break
            # 处理完黑名单后，再次查询是否还有黑名单，如果没有则再次查找原来的元素
            return self.find(by, value)
        # return self.driver.find_element(by, value)

    def swipe_find(self, text, num=3):
        # num = 3
        for i in range(0, num):
            if i == num - 1:
                raise NoSuchElementException(f"找了{num - 1}没有找到元素")

            try:
                return self.find(MobileBy.XPATH, f"//*[@text='{text}']")
            except:
                print("未找到，滑动")
                # 'width', 'height'
                size = self._driver.get_window_size()
                width = size['width']
                height = size['height']

                startx = width / 2
                starty = height * 0.8
                endx = startx
                endy = height * 0.3

                duration = 2000  # 2s
                self._driver.swipe(startx, starty, endx, endy, duration)

    # 称为关键字驱动代码
    #功能，可以解析关键字文件，对文件中的字符串进行一一处理，从而实现关键字操作
    def run_steps(self,path,function_name):
        with open(path,encoding='utf-8') as f:
            #data格式：{'goto_market':[{'action':'click','by':'xpath','express':'//*[@text="行情"]'}]}
            #函数名goto_market数据：[{'action':'','by':'','express':''},{},{},{}]
            data=yaml.safe_load(f)
        steps=data.get(function_name)
        # 每个一个step的格式是：{'action':'','by':'','express':''}
        for step in steps:
            #如果action键的值是click，代表想要点击元素
            if step.get('action')=='click':
                self.find(step.get('by'),step.get('express')).click()
            #相当于封装了输入框关键字
            elif step.get('action')=='send_keys':
                self.find(step.get('by'), step.get('express')).send_keys(step.get('content'))
                sleep(10)