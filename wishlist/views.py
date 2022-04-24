from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    """Render user's wishlist page."""

    return render(request, 'wishlist/wishlist.html')
