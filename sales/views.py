from django.shortcuts import render
from . models import SalesCamera 
# Create your views here.
def addSales(request):
    pagehead = "Sales"
    object = SalesCamera.objects.all()
    return render(request,"viewSales.html",{"stocks":object,"pagehead":pagehead})


