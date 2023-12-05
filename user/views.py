# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy

class MyLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('home_page')


def logout_view(request):
    logout(request)
    return redirect('login')