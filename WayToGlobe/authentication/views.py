from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
def login_view(request):
    form=LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('signup')
    context={'loginform':form}
    return render(request, 'login.html',context=context)

def signup_view(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('login')
    context={'registration':form}
    return render(request, 'signup.html',context=context)

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView

def forgot(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            return render(request, 'password_reset_done.html', {})
    else:
        return render(request, 'signup.html', {'form': form})
        form = PasswordResetForm()

    return render(request, 'password_reset.html', {'form': form}) 