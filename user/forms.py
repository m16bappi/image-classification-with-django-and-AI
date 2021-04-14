from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class loginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
