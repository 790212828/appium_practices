from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.homework.page.base_page import BasePage
from test_appium.homework.page.member_infomation_page import MemberInfomationPage


class ContactSearchPage(BasePage):
    def search(self,username):

        self.impactivity_sleep(10)#com.tencent.wework:id/g5f
        # WebDriverWait(self,10).until(lambda x:x.find(MobileBy.ID,'com.tencent.wework:id/g5f'))
        self.logger.debug(f"定位搜索输入框元素，然后输入成员姓名：{username}")
        self.find(MobileBy.ID,'com.tencent.wework:id/g5f').send_keys(username)


    def goto_member_infomation_page(self,username):
        self.logger.debug("通讯录页面查询成员姓名，点击成员列表按钮，然后进入个人信息页面")
        self.search(username)
        self.logger.debug("通过公司名字找上级再通过成员姓名定位，点击按钮")
        self.find(MobileBy.XPATH,f'//*[contains(@text,"测试公司")]/../..//*[@text="{username}"]').click()
        self.logger.debug("进入成员个人信息页面")
        return MemberInfomationPage(self._driver)

    def search_member_null(self,expect,username):
        self.logger.debug("通讯录页面查询成员信息，断言判断成员是否删除成功")
        self.search(username)
        result=self.find(MobileBy.XPATH,'//*[@text="无搜索结果"]').text

        self.assert_text(expect,result)


