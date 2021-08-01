from appium.webdriver.common.mobileby import MobileBy

from test_appium.homework.page.base_page import BasePage
from test_appium.homework.page.edit_contact_page import EditContactPage


class MemberInfomationPage(BasePage):

    def del_member_bymenual(self):
        self.logger.debug("个人信息页面，点击“编辑成员”按钮")
        self.impactivity_sleep(5)
        self.find(MobileBy.ID,"com.tencent.wework:id/hc9").click()
        self.find(MobileBy.XPATH,'//*[@text="编辑成员"]').click()
        self.logger.debug("进入成员编辑页面")
        return EditContactPage(self._driver)
