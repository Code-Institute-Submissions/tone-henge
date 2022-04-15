// Set page URL based on user's requested sort parameters.
$("#sort-by").change(function () {
    let selector = $(this);
    let currentUrl = new URL(location);

    let selectedVal = selector.val();
    if (selectedVal != "reset") {
        let sort = selectedVal.split("_")[0];
        let direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("order", direction);

        location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("order");

        location.replace(currentUrl);
    }
});
