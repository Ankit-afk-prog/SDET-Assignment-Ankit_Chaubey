"""Central test data/config. Browser and headless mode can be overridden via env vars."""
import os

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
BROWSER = os.getenv("BROWSER", "chrome").lower()          # chrome | firefox | edge
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
DEFAULT_TIMEOUT = int(os.getenv("TIMEOUT", "10"))

PASSWORD = "secret_sauce"
USERS = {
    "standard": "standard_user",
    "locked_out": "locked_out_user",
    "problem": "problem_user",
    "performance_glitch": "performance_glitch_user",
}

PRODUCT_NAME = "Sauce Labs Backpack"
PRODUCT_SLUG = "sauce-labs-backpack"

CUSTOMER = {"first_name": "Test", "last_name": "Tester", "postal_code": "440001"}

INVENTORY_URL_PART = "/inventory.html"
MSG_LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
MSG_INVALID_CREDS = "Epic sadface: Username and password do not match any user in this service"
MSG_ORDER_COMPLETE = "Thank you for your order!"
