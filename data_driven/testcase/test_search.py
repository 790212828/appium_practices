"""
查看相关的app包名：adb shell pm list package|findstr "browser"
查看浏览器版本信息：adb shell pm dump com.android.chrome |findstr "version"

#获取当前app包名 adb shell dumpsys window | findstr mCurrentFocus
#adb shell dumpsys activity | findstr mFocusedActivity

打开WEditor 可以用来定位
python -m weditor


查询包中chromedriver的版本信息：adb shell pm dump com.xueqiu.android |findstr "version"


"""
from test_appium.data_driven.page.app import App


class TestSearch:
    def setup_class(self):
        # self.app=App()
        pass

    def teardown_class(self):
        pass

    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")