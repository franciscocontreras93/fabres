from django import forms
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        mode = User
        fields = ['username','email','password','first_name','last_name']

    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


