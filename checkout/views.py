from django.shortcuts import render
from .forms import OrderForm


def checkout(request):
    """Render checkout template."""

    basket = request.session.get('basket', {})
    form = OrderForm()

    context = {
        'form': form,
        'stripe_public_key': 'pk_test_51KT9RqH5ISpKM2vGO5lXgKidD1xOUJSquTH3lyNG4xAsfGm0ow1FP5GBn0dCVAcB4JXVmO9faSzRmU31scIqLhgH009NWxgTQ7',
        'client_secret': 'test',
    }

    return render(request, 'checkout/checkout.html', context)
