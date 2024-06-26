from django.shortcuts import redirect, render
from rental.models import RentCamera
from .models import RentalBilling
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def rentcustomer(request, pk):
    if request.method == 'POST':
        itemToDisplay = RentCamera.objects.get(pk=pk)
        customer_name = request.POST.get('customer_name')
        customer_phno = request.POST.get('customer_phno')
        customer_address = request.POST.get('customer_address')
        customer_email = request.POST.get('customer_email')
        new_bill = RentalBilling(
            camera=itemToDisplay,
            customer_name=customer_name,
            customer_phno=customer_phno,
            customer_address=customer_address,
            customer_email=customer_email
        )
        new_bill.save()
        messages.success(request, 'Rental data added successfully!')
        itemToDisplay.isAvailable = 0
        itemToDisplay.save()
    
    itemToDisplay = RentCamera.objects.get(pk=pk)
    pagehead = "CustomerRentals"
    return render(request, "rental/bills/customerDetails.html", {"stock": itemToDisplay, "pagehead": pagehead})

@login_required
def viewRentalBills(request):
    pagehead = "Rentalbills"
    object = RentalBilling.objects.all()
    return render(request, "rental/bills/viewbills.html", {"bills": object, "pagehead": pagehead})

@login_required
def createRentalBills(request):
    pagehead = "Create Rental Bills"
    return render(request,"rental/bills/createbill.html",{"pagehead":pagehead})

@login_required
def deleteRentalBill(request, pk):
    itemToDelete = RentalBilling.objects.get(pk=pk)
    camera = itemToDelete.camera
    camera.isAvailable = 1
    camera.save()
    itemToDelete.delete()
    return redirect('viewRentalBills')