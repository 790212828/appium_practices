from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.homework.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self._driver=driver

    def addmember_bymenual(self):
        self.logger.debug("click 手动输入添加按钮，进入编辑成员页面")
        #click 手动输入添加按钮，进入编辑成员页面
        self.find(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.logger.debug("避免两个类互相导包造成异常，在方法局部内导包：test_appium.homework.pages.edit_contact_page")
        from test_appium.homework.page.edit_contact_page import EditContactPage
        return EditContactPage(self._driver)

    def verify_ok(self,expect):
        #返回上一页面,获取toast弹框 文本，进行断言
        self.logger.debug("返回上一页面,获取toast弹框 文本，进行断言")
        self.logger.debug("因为添加成功的toast提示是一瞬间显示后消失，这里需要用显示等待获取元素")
        WebDriverWait(self,10).until(lambda x:x.find(MobileBy.XPATH,"//*[@text='添加成功']"))
        result=self.find(MobileBy.XPATH,"//*[@text='添加成功']").text
        self.assert_text(expect,result)
