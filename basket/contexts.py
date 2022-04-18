from products.models import Product


def basket_contents(request):
    """Return basket information to template."""

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for product_id, quantity in basket.items():
        product = Product.objects.get(pk=product_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'product': product,
            'product_id': product_id,
            'quantity': quantity,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
    }

    return context
