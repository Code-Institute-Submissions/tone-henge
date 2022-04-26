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
