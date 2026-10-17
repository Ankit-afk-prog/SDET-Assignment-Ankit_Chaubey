# SDET Website Testing – Swag Labs (SauceDemo)

This project focuses on testing the Swag Labs demo website (https://www.saucedemo.com) through manual testing and automation using Python, Selenium WebDriver, and Pytest.

The aim was to test the website's main shopping features, identify bugs, document the issues, and automate a few important user journeys.

## What I Tested

The automated tests cover the following scenarios:

1. Successful login using "standard_user" and login failure with an incorrect password.
2. Adding a product to the cart, completing checkout, and verifying the order confirmation.
3. Checking that "locked_out_user" cannot log in and that the appropriate error message is displayed.

I also manually tested the login page, product catalog, sorting options, shopping cart, and checkout process. The detailed test cases are available in "TEST_PLAN.md", and the issues found during testing are documented in "BUG_REPORTS.md".

In addition to the accounts mentioned in the assignment, I tested "error_user" and "visual_user" to check how the website behaves with different user accounts.

## Tools and Technologies

- Python 3.10+
- Selenium WebDriver 4
- Pytest 8
- pytest-html
- Git and GitHub

I used the Page Object Model (POM) to organise the automation code and make it easier to maintain. Selenium Manager is used to handle browser driver setup automatically in most cases.

## Project Structure

```text
sdet-website-testing/
├── README.md
├── TEST_PLAN.md
├── BUG_REPORTS.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── tests/
│   ├── conftest.py
│   └── test_*.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── test_data/
│   └── test_config.py
├── reports/
└── screenshots/
```

The "tests" folder contains the automated test cases and shared fixtures. The "pages" folder contains the classes for individual website pages, while "test_data" stores the test configuration, including URLs, user credentials, and expected messages.

The "reports" folder is used to store HTML test reports, and "screenshots" contains screenshots captured when tests fail.

I also created "base_page.py" to keep commonly used browser actions and explicit-wait methods in one place.

## Requirements

Before running the project, make sure you have:

- Python 3.10 or later installed.
- Git installed.
- Chrome, Firefox, or Edge installed.
- An internet connection to access the demo website and download browser drivers when required.

To check your Python installation, run:

```bat
python --version
```

## Setup on Windows

Open Command Prompt and run these commands:

```bat
git clone <your-repo-url> sdet-website-testing
cd sdet-website-testing
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you are using PowerShell, activate the virtual environment with:

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, you may need to adjust the execution policy for the current session.

## Browser Configuration

The tests run in Chrome by default, with the browser window visible. You can change the browser and other settings using environment variables.
-----------------------------------------------
| Variable | Available values      | Default 
| BROWSER  | chrome, firefox, edge | chrome
| HEADLESS | true, false           | false 
| TIMEOUT  | Timeout in seconds    | 10
| BASE_URL | Website URL           | https://www.saucedemo.com 
----------------------------------------------------------------
For Command Prompt:

```bat
set BROWSER=firefox
set HEADLESS=true
```

For PowerShell:

```powershell
$env:BROWSER="firefox"
$env:HEADLESS="true"
```

## Running the Tests

To run all the automated tests, use:

```bat
pytest
```

To run an individual test file:

```bat
pytest tests\test_login.py
pytest tests\test_cart_checkout.py
pytest tests\test_locked_out_user.py
```
we can also run tests marked as smoke tests or negative tests:

```bat
pytest -m smoke
pytest -m
Project Links


Video 1 –  https://drive.google.com/file/d/1zSlvGcpraiF0Bdz3TuqRzEzzAt3yIauz/view?usp=sharing

Video 2 – https://drive.google.com/file/d/1_qHmoEGvO4N6xPwv0-gjzbX2aTC9rAks/view?usp=sharing