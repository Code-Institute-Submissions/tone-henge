from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product-view/<int:product_id>/', views.product_view, name='product_view')
]
