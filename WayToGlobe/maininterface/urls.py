from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.mainterface_view, name='main_interface'),
    path('search_car/', views.searchcar_view, name='search_car'),
    path('search_place/', views.searchplace_view,name='search_place'),
    path('search_place2/', views.searchplace_view2,name='search_place2'),
    path('search_car2/', views.searchcar_view2,name='search_car2')
    # Add more URL patterns as needed
]