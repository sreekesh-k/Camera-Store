from django.shortcuts import redirect, render
from sales.models import SalesCamera 
from . models import SalesBilling
# Create your views here.
def customer(request,pk):
    # if request.method == 'POST':

    itemToDisplay = SalesCamera.objects.get(pk=pk)
    pagehead = "CustomerDetails"
    return render(request,"CustomerDetails.html",{"stock":itemToDisplay,"pagehead":pagehead})