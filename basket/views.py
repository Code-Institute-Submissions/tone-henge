from django.shortcuts import render, redirect
from django.contrib import messages


def basket(request):
    """Render basket template."""

    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
    """
    Add specified quantity of an item to basket, checking that 
    the max quantity has not been reached.
    """

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        basket = request.session.get('basket', {})
        url = request.POST['redirect_url']

        if product_id in basket:

            if basket[product_id] + quantity > 99:
                if basket[product_id] == 99:
                    messages.add_message(
                        request, messages.WARNING, 'Max quantity reached.')

                    return redirect(url)

                messages.add_message(
                    request, messages.WARNING, f'Quantity in basket already \
                    too high. You can only add {99 - basket[product_id]} more \
                    of this item.')

                return redirect(url)

            basket[product_id] += quantity
        else:
            if quantity > 99 or quantity < 1:
                messages.add_message(
                    request, messages.WARNING,
                    'You may only add 1-99 of a product to your basket.')

                return redirect(url)

            basket[product_id] = quantity

        request.session['basket'] = basket

        messages.add_message(request, messages.SUCCESS,
                             f'Added {quantity} to basket.')

        return redirect(url)


def remove_from_basket(request, product_id):
    """Remove an item from basket."""

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        basket.pop(product_id)
        request.session['basket'] = basket

        messages.add_message(request, messages.SUCCESS,
                             'Successfully removed from basket.')

        return redirect('basket')


def adjust_quantity(request, product_id):
    """
    Update the quantity of an item currently in basket, ensuring
    the new quantity is within the allowed limit.
    """

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        new_quantity = request.POST['quantity']

        if new_quantity > 99 or new_quantity < 1:
            messages.add_message(
                request, messages.WARNING, 'You may only add 1-99 of a product\
                 to your basket.')

            return redirect('basket')

        basket[product_id] = int(new_quantity)
        request.session['basket'] = basket

        messages.add_message(request, messages.SUCCESS,
                             'Quantity updated successfully.')

        return redirect('basket')
