# urls.py
from django.urls import path
from .views import MyLoginView ,logout_view

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

]
