# Tone Henge Testing Documentation

## Validation

-   HTML
    -   HTML has been validated with no errors via the [W3C Markup Validator](https://validator.w3.org/).
-   CSS
    -   CSS has been validated with no errors or warnings via the [W3C Validator](https://jigsaw.w3.org/css-validator/).
-   Python
    -   Python has been validated with no errors via the [PEP8 Validator](http://pep8online.com).
-   JavaScript
    -   JavaScript has been validated with no errors via [JSHint](https://jshint.com/).

## Testing User Stories

-   As a Site User I can view all of the products on the site so I can see what is available.
    -   Products are easily and instantly available to a new or returning customer.
    -   Accessed via navigation links that are always accessible.
-   As a Site User I can view specific details about each product so I can find out more about the item.
    -   Each product has a dedicated 'details' page where the user can view further information.
    -   This page also contains links to further functionality such as adding an item to the basket.
    -   If the user is not authenticated, they will be prompted to sign in to access the features.
-   As a Site User I can easily view my basket total at any time so I can keep track of my order cost.
    -   Easily visible in the top right-hand corner of the site, the user is always aware of their current basket total.
    -   Total is calculated each time an item is added to the basket.
    -   Users can only add 1-99 of an item.
    -   If users remove HTML validation in dev tools and enter a number out of range, they will be shown an error message.
    -   The user is informed if they cannot add any more of an item to their basket.
-   As a Site User I can filter products so I am able to view them sorted in a format of my choice.
    -   Multiple filters are available for users to apply when viewing products.
    -   Filters behave as expected. Sorting is correct.
-   As a Site User I can sort by category so I am able to view only the type of products I am looking for.
    -   All products are assigned a category. They can then be sorted through by the user.
    -   Multiple categories are available as main navigation items, making it easy for the user to quickly choose one.
    -   Category sorting behaves as expected.
-   As a Site User I can search for products by name or description so I can find exactly what I'm looking for.
    -   Searching has been implemented in the navigation bar.
    -   This searches product name, description and related category and displays the results.
    -   If users remove HTML validation, backend checks still prevent the user searching over 50 characters.
-   As a Site User I can view the amount of search results after a particular search so I know how wide the range of results is.
    -   Search count is available at the top of all results, making it easy for users to quickly see.
    -   Manually tested across all categories and multiple searches. Always returns correct result.
-   As a Site User I can view my basket so I can see everything that has been added.
    -   Each item the user has added to their basket throughout the session is added to a session variable to be used across the site. The user can view each item in their basket.
    -   The basket displays items in the correct order, with correct and relevant information.
    -   Displayed total is always correct.
-   As a Site User I can adjust the quantity of an item in my basket so I can easily change my order without leaving the bag page.
    -   Users can adjust the quantity of an item in their basket directly.
    -   There are frontend checks to ensure the user doesn't add anything out of the desired range.
    -   If the user removes this check dev tools, there is a fallback backend check that ensures incorrect values will not be added and the user is notified.
-   As a Site User I can enter my payment details at checkout so I can proceed with my purchase.
    -   Form is available and functioning in the checkout app. This allows users to fill in their billing details.
    -   Payment detail fields have rigorous and responsive validation.
    -   User is informed of all errors specifically, e.g. not enough funds, incorrect card number, etc.
-   As a Site User I can pay for my basket of items securely so I can finalise my order.
    -   Stripe payments are implemented and registering correctly.
    -   Manual tests have confirmed payments are secure and consistently registering.
-   As a Site User I am shown a confirmation of my order so I know it was successful.
    -   Upon successful payment, the user is redirected to an order confirmation page.
    -   User is presented with relevant details to their order. Manually testing has confirmed these details are consistently correct and related to the correct order.
-   As a Site User I am able to sign up for an account so I can access functionality that requires authentication.
    -   Non-logged-in users are able to see prompts to sign in to access certain content across the site.
-   As an Authenticated User I am sent an email confirmation of my account creation so I know it was successful.
    -   Upon successful account creation, the user is sent a confirmation email.
    -   Emails have shown to always display correct data, with correct links leading back to the site.
-   As an Authenticated User I am able to log in or log out so I can change account.
    -   Simple logging in/out functionality implemented.
    -   When a user is logged in, they are made aware of their authenticated status.
    -   Users are prompted before signing out.
-   As a Site User I can get in touch via the website so I can raise any queries I may have.
    -   Users are able to register queries and their email.
    -   This information is being saved correctly in the database.
    -   Front/backend checks meaning users will still get error messages even if submitting with HTML validation removed in dev tools.
    -   Admin users are able to access an admin-specific page that allows them to view all user queries and emails.
    -   This page cannot be access by standard users. They will be redirected and given an error message.
-   As an Authenticated User I can leave a review/comment of a product so I can share my experience with others.
    -   When logged in, users have the option to leave comments on items.
    -   This feature cannot be accessed in any way by non-authenticated users.
    -   Users are able to edit and delete comments, but only their own.
    -   Validation is in place here again to prevent users from removing HTML validation in dev tools and submitting a comment over the character limit.
    -   When this happens, users are informed of the error and redirected.
-   As an Authenticated User I can add products to a wishlist so I can plan what to buy in the future.
    -   When logged in, users have the option to add products to their wishlist.
    -   Once authenticated, a button will be available on the products detail page.
    -   Once clicked, the user is given feedback that the item has been added. The button then switches to give the user the option to remove the item from their wishlist from the product page.
    -   User is also able to remove from the wishlist page directly.
    -   The wishlist displays the items in correct order with correct information.
    -   Users are directed to the link that the came from when removing a product.
    -   Non-authenticated users cannot access this feature.
-   Admin Operations
    -   Adding/Editing/Removing products works as expected.
    -   Changes are appropriately reflected in the database.
    -   Admin-only features.

## Further Testing

### Responsiveness

Tested using Firefox and Chrome across all viewports. Tested directly on a Galaxy S10, as well as a 15" laptop screen.

### General Tests

-   All links are working correctly and lead to the correct place.
-   Images are scaled and none are pixelated or blurred.
-   All authentication barriers are in place. Role-based authenticated has been implemented. Users across the site can only access what they are permitted to.
-   When logged in, account dropdown shows login status and gives option to logout.
-   When logged in, authentication-only features are visible, e.g. wishlist, commenting.
-   When logged out, users are prompted to sign in.
-   Long strings do not break any inputs as word break has been put in place.
-   Users are given feedback on all CRUD operations.
-   Users are asked for confirmation on all critical operations.
-   Buttons are easy to click for all users across devices.

## Bugs

### Current

### Solved

-   "The page footer covers part of the content on the page."
    -   This was solved by adding a content-container parent div with CSS to combat this.
-   "Items are being popped off of the basket when a user removes one, instead of the specific one being removed."
    -   The issue was that only a single modal was being loaded for confirming the deletion of an item, where there should have been one for each item. This was solved by adding a dynamic id to each element.
-   "Users are intended to have a maximum of 99 of a single item in their basket. HTML validation currently handles this, however this can be worked around if the user adds the item multiple times. For example, the user can add a 50 of a product 2 times, resulting in 100 total in the basket."
    -   A check was added at the point of the user adding an item to the basket that ensured they were not going to have a total quantity higher than the allowed limit.
-   "Non-authenticated users were unable to access product view pages."
    -   The implementation of the wishlist caused the above bug. This was due to a check in the view that assumed the user had a wishlist, which is not the case for non-authenticated users. This was fixed by ensuring request.user.is_authenticated was true before proceeding with the logic.
