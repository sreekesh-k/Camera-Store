from django.shortcuts import redirect, render
from sales.models import SalesCamera 
from . models import SalesBilling
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
    return render(request,"sales/bills/customerDetails.html",{"stock":itemToDisplay,"pagehead":pagehead})

@login_required
def viewSalesBills(request):
    pagehead = "SalesBills"
    object = SalesBilling.objects.all()
    return render(request,"sales/bills/viewbills.html",{"bills":object,"pagehead":pagehead})

@login_required
def createSalesBills(request):
    pagehead = "Create Sales Bills"
    return render(request,"sales/bills/createbill.html",{"pagehead":pagehead})

@login_required
def deleteSalesBills(request,pk):
    itemToDelete = SalesBilling.objects.get(pk=pk)
    camera = itemToDelete.camera
    camera.isAvailable=1
    camera.save()
    itemToDelete.delete()
    return redirect('viewSalesBills')