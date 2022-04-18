from django.shortcuts import redirect, render
from django.conf import settings
from .forms import OrderForm
from .models import OrderLineItem
from products.models import Product
from basket.contexts import basket_contents
import stripe


def checkout(request):
    """Render checkout template and handle form submission after purchase."""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_private_key = settings.STRIPE_PRIVATE_KEY
    basket = request.session.get('basket', {})

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()

            for product_id, quantity in basket.items():
                product = Product.objects.get(pk=product_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_line_item.save()

            return redirect('home')
        else:
            form = OrderForm()

    else:
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
