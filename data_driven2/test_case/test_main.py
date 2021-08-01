import pytest
import yaml

from test_appium.data_driven2.pages.app import App
from test_appium.data_driven2.test_case.test_base import TestBase


class TestMain(TestBase):
    # def setup(self):
    #     self.app = App()
    #
    # def teardown(self):
    #     # self._driver.quit()
    #     pass

    @pytest.mark.parametrize('value1,value2',yaml.safe_load(open('./test_main.yaml')))
    def test_main(self,value1,value2):

        self.app.start().main().goto_search()
        # print(value1)
        # print(value2)

    def test_windows(self):
        self.app.start().main().goto_windows()
