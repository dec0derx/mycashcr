from django.shortcuts import render, redirect
from django.urls import path
from . import views

urlpatterns = [
    path('exchangeRateCR', views.exchange_rate, name="exchange-rate"),
]