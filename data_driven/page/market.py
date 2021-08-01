from test_appium.data_driven.page.base_page import BasePage
from test_appium.data_driven.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../pages/market.yaml")
        return Search(self._driver)







