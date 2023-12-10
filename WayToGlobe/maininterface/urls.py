from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.mainterface_view, name='main_interface'),
    path('search_car/', views.searchcar_view, name='search_car')

    # Add more URL patterns as needed
]