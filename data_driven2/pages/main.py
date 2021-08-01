from time import sleep

from selenium.webdriver.common.by import By

from test_appium.data_driven2.pages.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        sleep(3)
        # self.find(By.ID,'tv_search').click()
        self.steps("../pages/main.yaml")

    def goto_windows(self):

        self.find(By.ID,'post_status').click()
        self.find(By.ID,'tv_search').click()















