from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())