import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from test_data import test_config as cfg


@pytest.mark.smoke
def test_add_to_cart_and_complete_checkout(logged_in_driver):
    d = logged_in_driver
    inventory = InventoryPage(d)

    inventory.add_to_cart(cfg.PRODUCT_SLUG)
    assert inventory.cart_count() == "1"

    inventory.open_cart()
    cart = CartPage(d)
    assert cart.item_names() == [cfg.PRODUCT_NAME]

    cart.checkout()
    checkout = CheckoutPage(d)
    c = cfg.CUSTOMER
    checkout.fill_customer_info(c["first_name"], c["last_name"], c["postal_code"])
    assert checkout.summary_items() == [cfg.PRODUCT_NAME]

    checkout.finish()
    assert checkout.confirmation_text() == cfg.MSG_ORDER_COMPLETE
    assert "checkout-complete" in d.current_url
