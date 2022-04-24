from django.shortcuts import render


def wishlist(request):
    """Render user's wishlist page."""

    return render(request, 'wishlist/wishlist.html')
