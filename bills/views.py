from django.shortcuts import redirect, render
from sales.models import SalesCamera 
from . models import SalesBilling
from django.contrib import messages
# Create your views here.
def customer(request,pk):
    if request.method == 'POST':
        itemToDisplay = SalesCamera.objects.get(pk=pk)
        customer_name = request.POST.get('customer_name')
        customer_phno = request.POST.get('customer_phno')
        customer_address =request.POST.get('customer_address')
        customer_email =request.POST.get('customer_email')
        new_bill = SalesBilling(camera=itemToDisplay,customer_name=customer_name,customer_phno=customer_phno,
                                            customer_address=customer_address,customer_email=customer_email,
                                            sales_price=itemToDisplay.MRP
                                            )
        new_bill.save()
        messages.success(request, 'Sales data added successfully!') 
        itemToDisplay.isAvailable=0
        itemToDisplay.save()
    itemToDisplay = SalesCamera.objects.get(pk=pk)
    pagehead = "CustomerDetails"
    return render(request,"CustomerDetails.html",{"stock":itemToDisplay,"pagehead":pagehead})