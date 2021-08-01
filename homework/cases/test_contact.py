"""
查看相关的app包名：adb shell pm list package|findstr "browser"
查看浏览器版本信息：adb shell pm dump com.android.chrome |findstr "version"

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity

打开WEditor 可以用来定位
python -m weditor


查询包中chromedriver的版本信息：adb shell pm dump com.xueqiu.android |findstr "version"


"""
from test_appium.homework.page.app import App
import sys
sys.path.append("..")


class TestContact:

    def setup_class(self):
        #打开应用，进入首页
        self.app=App()

    def setup(self):
        self.main=self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()



    def test_addcontact(self):
        username = "test1"
        phonenumber = "131606000001"
        assert_text="添加成功"
        self.main.goto_contactlistpage().goto_addmemberpage().addmember_bymenual().edit_memeber(username,phonenumber).verify_ok(assert_text)
    def test_addcontact2(self):
        assert_text = "添加成功"
        username = "test2"
        phonenumber = "13160600002"
        self.main.goto_contactlistpage().goto_addmemberpage().addmember_bymenual().edit_memeber(username,phonenumber).verify_ok(assert_text)


    def test_delcontact(self):
        username = "test1"
        assert_text="无搜索结果"
        self.main.goto_contactlistpage().goto_contact_search_page().goto_member_infomation_page(username).del_member_bymenual().del_member().search_member_null(assert_text,username)
    def test_delcontact2(self):
        username = "test2"
        assert_text="无搜索结果"
        self.main.goto_contactlistpage().goto_contact_search_page().goto_member_infomation_page(username).del_member_bymenual().del_member().search_member_null(assert_text,username)











