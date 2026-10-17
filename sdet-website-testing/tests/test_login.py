import pytest

from pages.inventory_page import InventoryPage
from test_data import test_config as cfg


@pytest.mark.smoke
def test_successful_login(login_page):
    login_page.login(cfg.USERS["standard"])
    login_page.wait_for_url_contains(cfg.INVENTORY_URL_PART)

    inventory = InventoryPage(login_page.driver)
    assert inventory.title() == "Products"
    assert inventory.item_count() == 6


@pytest.mark.negative
def test_invalid_password_rejected(login_page):
    login_page.login(cfg.USERS["standard"], "wrong_password")

    assert cfg.MSG_INVALID_CREDS in login_page.error_message()
    assert cfg.INVENTORY_URL_PART not in login_page.driver.current_url
