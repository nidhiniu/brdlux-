from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

     

class RegisterUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email']  

class profileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class Carform(forms.ModelForm):
    class Meta:
        model=Car
        fields="__all__"

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        # fields="__all__"
        exclude=['user']

