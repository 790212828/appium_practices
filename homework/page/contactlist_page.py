from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.homework.page.add_member_page import  AddMemberPage
from test_appium.homework.page.base_page import BasePage
from test_appium.homework.page.contact_search_page import ContactSearchPage


class ContactListPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self._driver=driver

    def goto_addmemberpage(self):
        self.logger.debug("click 点击添加成员操作按钮，进入添加成员页面")
        self.impactivity_sleep(5)
        #click 点击添加成员操作按钮，进入添加成员页面
        # self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                           'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
        #                           '.scrollIntoView(new UiSelector().text("添加成员")'
        #                           '.instance(0));').click()
        self.logger.debug("开始滑动查找：添加成员按钮")
        self.swipe_find("添加成员").click()
        return AddMemberPage(self._driver)

    def goto_contact_search_page(self):
        self.logger.debug("在通行录页面，点击“搜索”图标按钮")
        self.impactivity_sleep(5)
        self.find(MobileBy.ID,"com.tencent.wework:id/hci").click()
        self.logger.debug("跳转到通讯录查询页面")
        return ContactSearchPage(self._driver)









