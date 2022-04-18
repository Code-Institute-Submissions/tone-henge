const stripePublicKey = $("#stripe_public_key").text().slice(1, -1);
const clientSecret = $("#client_secret").text().slice(1, -1);

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
    document.querySelector("#card-error").innerHTML = event.error
        ? `<span>${alertIcon}</span> ${event.error.message}`
        : "";
});

// Handle form submission
const form = document.getElementById("payment-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    payWithCard(stripe, card, clientSecret);
});

let payWithCard = function (stripe, card, clientSecret) {
    stripe
        .confirmCardPayment(clientSecret, {
            payment_method: {
                card: card
            }
        })
        .then(function (result) {
            if (result.error) {
                alertIcon = '<i class="fas fa-exclamation-circle"></i>';
                message = `<span>${alertIcon}</span> ${result.error.message}`;
                document.querySelector("#card-error").innerHTML = message;
            } else {
                form.submit();
            }
        });
};
