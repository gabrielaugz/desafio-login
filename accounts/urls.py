# accounts/urls.py
from django.urls import path
from .views import login_view, register_view, menu_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('menu/', menu_view, name='menu'),
]