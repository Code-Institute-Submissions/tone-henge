from django.urls import path
from . import views

urlpatterns = [
    path('add_comment/<product_id>', views.add_comment, name='add_comment'),
]
