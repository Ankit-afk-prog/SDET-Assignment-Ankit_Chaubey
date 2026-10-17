"""Fixtures: browser setup/teardown, logged-in session, failure screenshots."""
import base64
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.login_page import LoginPage
from test_data import test_config as cfg

ROOT = Path(__file__).resolve().parent.parent
SHOT_DIR = ROOT / "screenshots"


def _build_driver():
    if cfg.BROWSER == "chrome":
        opts = ChromeOptions()
        # Suppress Chrome's password-manager / breach popups that can block clicks.
        opts.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        })
        opts.add_argument("--window-size=1366,900")
        if cfg.HEADLESS:
            opts.add_argument("--headless=new")
        return webdriver.Chrome(options=opts)
    if cfg.BROWSER == "firefox":
        opts = FirefoxOptions()
        if cfg.HEADLESS:
            opts.add_argument("-headless")
        return webdriver.Firefox(options=opts)
    if cfg.BROWSER == "edge":
        opts = EdgeOptions()
        opts.add_argument("--window-size=1366,900")
        if cfg.HEADLESS:
            opts.add_argument("--headless=new")
        return webdriver.Edge(options=opts)
    raise ValueError(f"Unsupported BROWSER '{cfg.BROWSER}'. Use chrome, firefox or edge.")


@pytest.fixture
def driver():
    """Fresh browser per test => clean cart/session, so tests are repeatable."""
    drv = _build_driver()
    yield drv
    drv.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).open()


@pytest.fixture
def logged_in_driver(driver):
    page = LoginPage(driver).open()
    page.login(cfg.USERS["standard"])
    page.wait_for_url_contains(cfg.INVENTORY_URL_PART)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """On test failure save a PNG to screenshots/ and embed it in the HTML report."""
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    drv = item.funcargs.get("driver")
    if drv is None:
        return
    try:
        SHOT_DIR.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = SHOT_DIR / f"{item.name}_{stamp}.png"
        drv.save_screenshot(str(path))
        try:
            from pytest_html import extras
            b64 = base64.b64encode(path.read_bytes()).decode()
            report.extras = getattr(report, "extras", []) + [extras.png(b64)]
        except ImportError:
            pass
    except Exception as exc:  # never let screenshot problems mask the real failure
        print(f"Could not capture screenshot: {exc}")
