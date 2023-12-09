from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.mainterface_view, name='main_interface'),

    # Add more URL patterns as needed
]