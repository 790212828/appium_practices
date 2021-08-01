from test_appium.test_ui_framework.ui_framework.app import App


class TestGoToMarket:
    def setup(self):
        self.app=App().start()

    def test_goto_market(self):
        self.app.goto_main().goto_market()