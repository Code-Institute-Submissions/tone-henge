from django.shortcuts import render, redirect


def basket(request):
    """Render basket template."""

    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
    """Add certain quantity of an item to basket."""

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        basket = request.session.get('basket', {})
        url = request.POST['redirect_url']

        if product_id in basket:
            basket[product_id] += quantity
        else:
            basket[product_id] = quantity

        request.session['basket'] = basket

        return redirect(url)


def remove_from_basket(request, product_id):
    """Remove an item from basket."""

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        basket.pop(product_id)
        request.session['basket'] = basket

        return redirect('basket')


def adjust_quantity(request, product_id):
    """Update the quantity of an item currently in basket."""

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        new_quantity = request.POST['quantity']
        basket[product_id] = int(new_quantity)
        request.session['basket'] = basket

        return redirect('basket')
