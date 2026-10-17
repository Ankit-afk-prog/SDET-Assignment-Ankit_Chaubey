from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH = (By.CSS_SELECTOR, "[data-test='finish']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    SUMMARY_ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

    def fill_customer_info(self, first, last, postal):
        self.type(self.FIRST, first)
        self.type(self.LAST, last)
        self.type(self.POSTAL, postal)
        self.click(self.CONTINUE)

    def summary_items(self):
        return [e.text for e in self.find_all(self.SUMMARY_ITEM_NAMES)]

    def finish(self):
        self.click(self.FINISH)

    def confirmation_text(self) -> str:
        return self.text_of(self.COMPLETE_HEADER)

    def error_message(self) -> str:
        return self.text_of(self.ERROR)
