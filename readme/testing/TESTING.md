# Tone Henge Testing Documentation

## Bugs

### Current

-   Users are intended to have a maximum of 99 of a single item in their basket. HTML validation currently handles this, however this can be worked around if the user adds the item multiple times. For example, the user can add a 50 of a product 2 times, resulting in 100 total in the basket.
-   Items are being popped off of the basket when a user removes one, instead of the specific one being removed.

### Solved

-   The page footer covers part of the content on the page. This was solved by adding a content-container parent div with CSS to combat this.
