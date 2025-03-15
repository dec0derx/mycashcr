from django.shortcuts import render, redirect
from django.urls import path
from . import views

urlpatterns = [
    path('salaryCalculator', views.salary_calculator, name="salary-calculator")
]