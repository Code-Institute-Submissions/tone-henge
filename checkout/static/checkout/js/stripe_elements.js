const stripePublicKey = $("#stripe_public_key").text().slice(1, -1);
const client_secret = $("#client_secret").text().slice(1, -1);

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
    base: {
        color: "#000",
        fontFamily: "Arial, sans-serif",
        fontSmoothing: "antialiased",
        fontSize: "16px",
        lineHeight: "1.5",
        "::placeholder": {
            color: "#000"
        }
    },
    invalid: {
        fontFamily: "Arial, sans-serif",
        color: "#fa755a",
        iconColor: "#fa755a"
    }
};
const card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle validation errors in card element
card.on("change", function (event) {
    alertIcon = '<i class="fas fa-exclamation-circle"></i>';
    message = `<span>${alertIcon}</span> ${event.error.message}`;
    document.querySelector("#card-error").innerHTML = event.error
        ? message
        : "";
});
