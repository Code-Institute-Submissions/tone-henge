from django.shortcuts import render
from .forms import UserQueryForm


def contact(request):
    """Render contact page and handle form submission for user queries."""

    form = UserQueryForm()

    context = {'form': form, }

    return render(request, 'contact/contact.html', context)
