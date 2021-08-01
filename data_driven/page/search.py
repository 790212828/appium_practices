from test_appium.data_driven.page.base_page import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"]=value
        self.steps("../page/search.yaml")



