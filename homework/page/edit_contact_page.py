# from test_appium.homework.pages.add_member_page import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.homework.page.base_page import BasePage


class EditContactPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self._driver=driver

    def edit_memeber(self,username,phonenumber):
        self.logger.debug("进入成员编辑页面，输入姓名、电话号码，点击保存后；再跳转页面")
        self.logger.debug(f"输入的姓名：{username}，手机号码：{phonenumber}")
        """

        :param username: 输入新增的成员姓名
        :param phonenumber: 输入新增的成员电话号码
        :return: 保存成功后会跳转到添加成员页面，返回添加成员页面类
        """
        self.impactivity_sleep(10)

        self.find(MobileBy.XPATH,'//*[contains(@text,"姓名")]/..//*[@class="android.widget.EditText"]').send_keys(username)
        self.find(MobileBy.XPATH,'//*[contains(@text,"+86")]/../..//*[@class="android.widget.EditText"]').send_keys(phonenumber)
        self.find(MobileBy.XPATH,'//*[@text="保存"]').click()

        # 返回上一个页面
        self.logger.debug("避免两个类互相导包造成异常，在方法局部内导包：test_appium.homework.pages.add_member_page")
        from test_appium.homework.page.add_member_page import AddMemberPage
        return AddMemberPage(self._driver)


    def del_member(self):
        self.logger.debug("从个人信息页面进入编辑页面，查询删除按钮，点击删除按钮，跳转返回上一个页面")
        self.impactivity_sleep(5)
        self.logger.debug("滑动查找“删除成员”按钮")
        self.swipe_find("删除成员").click()
        self.logger.debug("点击完删除成员按钮后，会弹出toast提示框，让用户再次确认是否删除")
        self.logger.debug("这里需要显示等待toast提示框弹出在进行点击")
        WebDriverWait(self,10).until(lambda x:x.find(MobileBy.XPATH,'//*[@text="删除成员"]/../..//*[@text="确定"]'))
        self.find(MobileBy.XPATH,'//*[@text="删除成员"]/../..//*[@text="确定"]').click()

        self.logger.debug("避免两个类互相导包造成异常，在方法局部内导包：test_appium.homework.pages.contact_search_page")
        from test_appium.homework.page.contact_search_page import ContactSearchPage
        return ContactSearchPage(self._driver)
