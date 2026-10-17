from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from test_data import test_config as cfg


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "[data-test='login-button']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(cfg.BASE_URL)
        self.find(self.LOGIN_BTN)
        return self

    def login(self, username, password=cfg.PASSWORD):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def error_message(self) -> str:
        return self.text_of(self.ERROR)
