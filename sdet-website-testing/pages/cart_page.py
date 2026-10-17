from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-test='checkout']")

    def item_names(self):
        return [e.text for e in self.find_all(self.ITEM_NAMES)]

    def checkout(self):
        self.click(self.CHECKOUT_BTN)
