from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def mainterface_view(request):
    return render(request, 'index.html')

def searchcar_view(request):
    return render(request, 'search_car.html')