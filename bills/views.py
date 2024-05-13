from django.shortcuts import redirect, render
from sales.models import SalesCamera 
from . models import SalesBilling
# Create your views here.
def customer(request,pk):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_phno = request.POST.get('customer_phno')
        customer_address =request.POST.get('customer_address')
        customer_email =request.POST.get('customer_email')
        new_bill = SalesBilling(camera=pk,customer_name=customer_name,customer_phno=customer_phno,
                                            customer_address=customer_address,customer_email=customer_email
                                            )
    
    
    pagehead = "CustomerDetails"
    return render(request,"CustomerDetails.html",{"stock":itemToDisplay,"pagehead":pagehead})