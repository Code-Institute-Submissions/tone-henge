from locale import currency
from django.shortcuts import render
from django.conf import settings
from .forms import OrderForm
from basket.contexts import basket_contents
import stripe


def checkout(request):
    """Render checkout template."""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_private_key = settings.STRIPE_PRIVATE_KEY

    basket = request.session.get('basket', {})
    form = OrderForm()
    current_basket = basket_contents(request)
    total = current_basket['total']

    stripe_total = round(total * 100)
    stripe.api_key = stripe_private_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total, currency=settings.STRIPE_CURRENCY)

    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
