from django.shortcuts import render

# Create your views here.

def salary_calculator(request):
    return render(request, "salaryCalculator/salary_calculator.html")
