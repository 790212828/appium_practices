from test_appium.data_driven2.pages.app import App


class TestBase:
    def setup(self):
        self.app=App()
    def teardown(self):
        self.app.stop()