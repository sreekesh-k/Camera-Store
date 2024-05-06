from django.shortcuts import render

# Create your views here.
def addSales(request):
    pagehead = "Sales"
    return render(request,"addSales.html",{"pagehead":pagehead})


