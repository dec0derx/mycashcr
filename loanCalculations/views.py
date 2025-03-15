from django.shortcuts import render

# Create your views here.

def loanCalculation (request):
    if request.method == "POST":
        print(request.POST["loan_amount"])
        print(request.POST["interest_rate"])
        print(request.POST["months"])

        monthy_payment = monthly_loan(float(request.POST["loan_amount"]),float(request.POST["interest_rate"]),float(request.POST["months"]))
        

        messages = [monthy_payment]
        args = {'results': messages}

        return render(request, "loanCalculations/monthly_payment.html", args)

    return render(request, "loanCalculations/monthly_payment.html")

def monthly_loan(principal,interest_rate,duration):
    n = duration            #total number of months
    r = interest_rate/(100*12) #interest per month
    monthly_payment = principal*((r*((r+1)**n))/(((r+1)**n)-1)) #formula for compound interest applied on mothly payments.
    monthly_payment = round(monthly_payment, 2)
    print(monthly_payment)
    return monthly_payment

