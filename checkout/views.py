from django.shortcuts import render
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    form = OrderForm()

    context = {'form': form, }

    return render(request, 'checkout/checkout.html', context)
