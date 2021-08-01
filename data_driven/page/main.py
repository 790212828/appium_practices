from test_appium.data_driven.page.base_page import BasePage
from test_appium.data_driven.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../pages/main.yaml")
        return Market(self._driver)