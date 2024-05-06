from django.shortcuts import render
from . models import SalesCamera 
# Create your views here.
def viewSales(request):
    pagehead = "Sales"
    object = SalesCamera.objects.all()
    return render(request,"viewSales.html",{"stocks":object,"pagehead":pagehead})


def addSales(request):
    pagehead = "Add Sales"
    return render(request,"addSales.html",{"pagehead":pagehead})