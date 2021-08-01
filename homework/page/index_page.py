from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.homework.page.base_page import BasePage
from test_appium.homework.page.contactlist_page import ContactListPage


class IndexPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self._driver=driver
    def goto_contactlistpage(self):
        self.logger.debug("主页面，操作点击通讯录")
        self.impactivity_sleep(10)
        #click 点击进入通讯录页面
        self.find(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        # locator = (MobileBy.XPATH, '//*[@text="通讯录"]')
        # self.find(*locator).click()

        return ContactListPage(self._driver)