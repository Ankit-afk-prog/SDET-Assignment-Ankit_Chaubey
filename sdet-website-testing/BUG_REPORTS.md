Bug Reports – Swag Labs
Website: https://www.saucedemo.com  
Test environment: Windows [version], Google Chrome [version]  
Password for all test accounts: "secret_sauce"
The following issues were observed while testing Swag Labs using different user accounts. Severity and priority are based on the impact each issue may have on users.
Bug Summary
| Bug-ID  |  User Account   | Module          | Issue                                            | Severity | Priority | Status
| BUG-001 | `problem_user` | Product Catalog | Same image displayed for different products      | Medium   | High     | Reproduced
| BUG-002 | `problem_user` | Product Catalog | Add to Cart option missing on some products      | High     | High     | Needs item details
| BUG-003 | `problem_user` | Cart            | Unable to remove items from cart                 | Medium   | Medium   | Needs retesting
| BUG-004 | `problem_user` | Sorting         | Product sorting not working correctly            | Medium   | Medium   | Needs retesting
| BUG-005 | `problem_user` | Checkout        | Last Name field does not accept input            | High     | High     | Needs retesting
| BUG-006 | `error_user`   | Sorting         | Sorting displays an error alert                  | Medium   | Medium   | Reproduced
| BUG-007 | `error_user`   | Checkout        | Last Name field does not accept input            | High     | High     | Needs retesting
| BUG-008 | `error_user`   | Cart            | Unable to remove items from cart                 | Medium   | Medium   | Needs retesting
| BUG-009 | `visual_user`  | Sorting         | Products appear in the wrong order after sorting | Medium   | Medium   | Needs retesting

BUG-001: Same Image Displayed for Different Products
Module: Product Catalog  
User account: "problem_user"  
Severity: Medium | Priority: High
Steps to reproduce:
Open the Swag Labs website.
Log in using "problem_user" and the password "secret_sauce".
Open the Products page.
Compare the images displayed for different products.
Expected result: Each product should display its correct image.
Actual result:Several products display the same dog image even though their names and descriptions are different.
Impact: Users may get the wrong impression of a product before adding it to their cart. This can reduce trust in the website and lead to incorrect purchase decisions.

Status Reproduced.
BUG-002: Add to Cart Option Missing on Some Products
Module: Product Catalog / Cart  
User account : "problem_user"
Severity: High | Priority: High
Steps to reproduce
Log in using "problem_user".
Open the Products page.
Check the Add to Cart buttons for the available products.
Try adding the affected products to the cart.
Expected result: Each available product should have a working Add to Cart button.
Actual result: The Add to Cart option was missing or unavailable for some products during testing.
Impact: Users may be unable to add the products they want to purchase, which interrupts the shopping process.

Status: Observed. The exact affected products need to be listed before the report is finalized.

BUG-003: Unable to Remove Items from Cart
Module: Shopping Cart  
User account: "problem_user"  
Severity: Medium | Priority: Medium
Steps to reproduce:
Log in using "problem_user".
Add a product to the cart.
Open the cart page.
Click Remove next to the selected product.
Expected result: The selected product should disappear from the cart, and the cart count should update.
Actual result: The product reportedly remains in the cart after clicking Remove.
Impact: Users may be unable to correct their cart before checkout.
Status: Reported during testing; retest before marking as confirmed.
---
BUG-004: Product Sorting Not Working Correctly
Module: Product Sorting
User account: "problem_user"
Severity: Medium | Priority: Medium
Steps to reproduce:
Log in using "problem_user".
Open the sorting dropdown on the Products page.
Select Name (A to Z).
Repeat with Name (Z to A), Price (low to high), and Price (high to low).
Check whether the products appear in the expected order.
Expected result: The product list should change according to the selected sorting option.
Actual result: Sorting reportedly did not work correctly for the options tested.
Impact: Users may have difficulty finding products or comparing prices.
Status: Needs retesting. Record the result of each sorting option separately.
---
BUG-005: Last Name Field Does Not Accept Input
Module: Checkout – Your Information
User account: "problem_user"
Severity: High | Priority: High
Steps to reproduce:
Log in using "problem_user".
Add a product to the cart and proceed to checkout.
Open the Your Information page.
Click the Last Name field and try entering a name.
Fill in the other required fields and click Continue.
Expected result: The Last Name field should accept text, and the user should be able to continue after completing the required information.
Actual result: The Last Name field reportedly did not accept input. The page displayed the message "Error: Last Name is required".
Impact: If the field cannot accept input, the user cannot proceed with checkout or complete an order.
Screenshot: "screenshots/BUG-005_problem_user_lastname_error.png"
Status: Observed. Repeat the test once more to confirm the behavior.
---
BUG-006: Sorting Displays an Error Alert
Module: Product Sorting
User account: "error_user"
Severity: Medium | Priority: Medium
Steps to reproduce:
Log in using "error_user".
Open the Products page.
Open the sorting dropdown.
Select a sorting option.
Expected result: The products should be sorted without displaying an error.
Actual result: A browser alert appears with the message:
"Sorting is broken! This error has been reported to Backtrace."
Impact: Users cannot reliably use the sorting feature, and the error interrupts their shopping experience.

Status: Reproduced. The alert is visible in the captured screenshot.
---
BUG-007: Last Name Field Does Not Accept Input
Module: Checkout – Your Information
User account: "error_user"
Severity: High | Priority: High
Steps to reproduce:
Log in using "error_user".
Add a product to the cart and proceed to checkout.
Click the Last Name field.
Try entering a name and then click Continue.
Expected result: The field should accept the entered name, allowing the user to proceed when all required fields are completed.
Actual result: The field reportedly did not accept input, preventing the user from completing the checkout information.
Impact: Users may be unable to finish their orders.
Status: Needs another check to confirm the field itself is not accepting input.
---
BUG-008: Unable to Remove Items from Cart
Module: Shopping Cart
User account: "error_user"
Severity: Medium | Priority: Medium
Steps to reproduce:
Log in using "error_user".
Add a product to the cart.
Open the cart page.
Click Remove next to the product.
Expected result: The selected product should be removed from the cart.
Actual result: The product reportedly remains in the cart after clicking Remove.
Impact: Users may be unable to change their selected items before checkout.
Status: Needs retesting to confirm that the item remains in the cart after the action.
---
BUG-009: Products Appear in the Wrong Order After Sorting
Module: Product Sorting
User account: "visual_user"
Severity: Medium | Priority: Medium
Steps to reproduce:
Log in using "visual_user".
Open the Products page.
Select Name (A to Z) and check the product order.
Repeat with Name (Z to A), Price (low to high), and Price (high to low).
Compare the displayed order with the selected option.
Expected result: Products should appear in alphabetical or price order, depending on the selected option.
Actual result: The product order reportedly did not match the selected sorting option.
Impact: Users may find it harder to locate products and compare prices.
Status: Needs another check. Record which sorting options produce the incorrect order before treating this as a confirmed bug.
---
Additional Observations
Performance delays
While using "performance_glitch_user", some actions, including login, sorting, adding products, and removing products, appeared slow at times. I did not measure the response times, so I have not listed this as a confirmed bug. It would be worth repeating these actions and recording the response times before reporting a performance issue.
Checkout button placement
The Checkout button appeared near the upper-right corner of the page in the screenshot. Its position alone does not confirm a defect. It should be reported as a UI bug only if further testing shows that it is hidden, clipped, difficult to access, or not working at a relevant screen size.
Final Notes
These reports are based on the behavior observed during manual testing. Issues marked for retesting should be reproduced again before submission. The screenshots should be saved using the filenames listed in each report so that the evidence is easy to match with the corresponding bug.
Severity and priority are initial assessments and may change after further testing.