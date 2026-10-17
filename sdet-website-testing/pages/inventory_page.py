from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def title(self) -> str:
        return self.text_of(self.TITLE)

    def item_count(self) -> int:
        return len(self.find_all(self.ITEMS))

    def add_to_cart(self, slug: str):
        self.click((By.CSS_SELECTOR, f"[data-test='add-to-cart-{slug}']"))

    def cart_count(self) -> str:
        return self.text_of(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)
