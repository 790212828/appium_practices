#雪球的首页page
#可以直接继承basepage,调用底层已经封装好的UI操作
#By.XPATH=="xpath"
import yaml
from selenium.webdriver.common.by import By

from test_appium.test_ui_framework.ui_framework.base_page import BasePage


class IndexPage(BasePage):

    def goto_market(self):
        # self.find('xpath','//*[@text="行情"]').click()
        # with open('../page/index_page.yaml',encoding='utf-8') as f:
        #     #data格式：{'goto_market':[{'action':'click','by':'xpath','express':'//*[@text="行情"]'}]}
        #     #函数名goto_market数据：[{'action':'','by':'','express':''},{},{},{}]
        #     data=yaml.safe_load(f)
        # steps=data.get("goto_market")
        # #每个一个step的格式是：{'action':'','by':'','express':''}
        # for step in steps:
        #     #如果action键的值是click，代表想要点击元素
        #     if step.get('action')=='click':
        #         self.find(step.get('by'),step.get('express')).click()
        self.run_steps('../page/index_page.yaml','goto_market')