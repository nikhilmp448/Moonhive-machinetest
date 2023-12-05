# Create a forms.py file in your app and add the following code

from django import forms
from .models import Account
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['email', 'password']

