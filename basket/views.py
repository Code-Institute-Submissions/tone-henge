from django.shortcuts import render, redirect


def basket(request):
    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
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
    if request.method == 'POST':
        basket = request.session.get('basket', {})
        basket.pop(product_id)
        request.session['basket'] = basket

        return redirect('basket')
