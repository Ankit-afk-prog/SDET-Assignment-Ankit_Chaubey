# Test Plan: Swag Labs (SauceDemo)

Website: https://www.saucedemo.com

Field Details
Author Ankit Chaubey
Version 1.1 
Manual testing Login, sorting, cart, and checkout were tested on the accounts listed in Section 5. Results are recorded in Section 6. 
Automated testingTest scripts have been prepared. The results will be added to the README after running the suite. 

## 1. Objective

The purpose of this testing was to check the main features of Swag Labs, including login, browsing products, sorting, managing the cart, and completing checkout. I also explored the website using different user accounts to identify issues and document their impact.

The plan covers manual testing as well as automated tests for the most important user flows.

## 2. Scope

Features included in testing:

- Login and logout
- Product catalog and product details
- Product sorting
- Adding and removing items from the cart
- Checkout and order confirmation
- Menu and navigation

Features not covered in this assignment:

- Load and performance benchmarking
- Security testing
- Backend and API testing
- Native mobile application testing

## 3. Types of Testing
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Testing type       | What I checked |
| Functional testing | Whether login, product browsing, sorting, cart, and checkout work as expected. |
| UI testing         | Product images, button availability, error messages, and page layout. |
| Negative testing   | Login with incorrect credentials, locked accounts, and empty checkout fields. |
| Boundary testing   | Very long usernames and inputs containing only spaces. |
| Exploratory testing| Tried different actions and user accounts, especially "problem_user", "error_user", and "visual_user". |
| Regression testing | Prepared Selenium and Pytest tests for important user flows. |
| Cross-browser testing | The test setup supports Chrome, Firefox, and Edge through the "BROWSER" environment variable. Actual browser coverage should be recorded after testing. |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 4. Test Environment
-------------------------------------------------------------------------------------
| Item             	| Details 
| Operating system 	| Windows 10/11 |
| Browsers         	| Chrome, Firefox, and Edge |
| Programming language  | Python 3.10 or later |
| Automation tools	| Selenium WebDriver 4 and Pytest 8 |
| Reporting 		| pytest-html |
| Version control 	| Git and GitHub |
| Test structure 	| Page Object Model (POM), with fixtures in "tests/conftest.py" |
----------------------------------------------------------------------------------------
The exact browser version should be added after checking the browser used during testing.

## 5. Test Data

All test accounts use the password "secret_sauce".
---------------------------------------------------------------------------------------------
| Username 			| Purpose |
| "standard_user"       	| Used to check normal website functionality. |
| "locked_out_user"    		| Used to verify that a locked account cannot log in. |
| "problem_user"        	| Used to check product images, cart actions, sorting, and checkout. |
| "performance_glitch_user"     | Used to observe delays during different actions. |
| "error_user"                  | Used to check sorting errors, cart behavior, and checkout. |
| "visual_user"                 | Used to check product sorting and visual behavior. |
--------------------------------------------------------------------------------------------------
The assignment specifically mentions the first four accounts. I also tested "error_user" and "visual_user" because they were available on the login page and helped me explore additional issues.

Checkout test data:

- First name: "Test"
- Last name: "Tester"
- Postal code: "440001"

## 6. Detailed Test Cases

The status indicates what happened during testing. "Auto" shows whether an automated test has been planned for that case.

TC-01: Standard User Login
Steps / Test Data: Log in using username "standard_user" and password "secret_sauce".
Expected Result: The inventory page should open and display the products.
Actual Result: Login worked, and the product page displayed normally. No issue was noticed.
Status: Pass
Automation: Yes

TC-02: Locked-Out User Login
Steps / Test Data: Log in using username "locked_out_user" and password "secret_sauce".
Expected Result: Login should be rejected with an error message.
Actual Result: Login was rejected, and an error message appeared.
Status: Pass
Automation: Yes

TC-03: Incorrect Password
Steps / Test Data: Use username "standard_user" with password "wrong_pass".
Expected Result: An appropriate login error should appear.
Actual Result: Not tested yet.
Status: Not Executed
Automation: Yes

TC-04: Empty Username
Steps / Test Data: Leave the username field empty and enter the password.
Expected Result: A username-required error should appear.
Actual Result: Not tested yet.
Status: Not Executed
Automation: No

TC-05: Empty Password
Steps / Test Data: Enter the username but leave the password field empty.
Expected Result: A password-required error should appear.
Actual Result: Not tested yet.
Status: Not Executed
Automation: No

TC-06: Very Long Username
Steps / Test Data: Enter a username containing 256 or more characters.
Expected Result: The website should handle the input properly without breaking the layout.
Actual Result: Not tested yet.
Status: Not Executed
Automation: No