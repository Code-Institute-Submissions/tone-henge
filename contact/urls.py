from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('view_queries', views.view_queries, name='view_queries')
]
