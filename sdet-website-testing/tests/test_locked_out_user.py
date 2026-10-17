import pytest

from test_data import test_config as cfg


@pytest.mark.negative
def test_locked_out_user_cannot_login(login_page):
    login_page.login(cfg.USERS["locked_out"])

    assert cfg.MSG_LOCKED_OUT in login_page.error_message()
    assert cfg.INVENTORY_URL_PART not in login_page.driver.current_url
