from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('<product_id>', views.add_to_basket, name='add_to_basket'),
    path('remove/<product_id>', views.remove_from_basket,
         name='remove_from_basket'),
    path('update/<product_id>', views.adjust_quantity, name='adjust_quantity'),
]
