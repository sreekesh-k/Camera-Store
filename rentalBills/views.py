from django.shortcuts import redirect, render
from rental.models import RentCamera
from .models import RentalBilling
from django.contrib import messages
# Create your views here.
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
    return render(request, "CustomerRentalDetails.html", {"stock": itemToDisplay, "pagehead": pagehead})

def viewRentalBills(request):
    pagehead = "Rentalbills"
    object = RentalBilling.objects.all()
    return render(request, "rentalbills.html", {"bills": object, "pagehead": pagehead})

def createRentalBills(request):
    pagehead = "createRentalBills"
    return render(request,"createRentalBills.html",{"pagehead":pagehead})

def deleteRentalBills(request, pk):
    itemToDelete = RentalBilling.objects.get(pk=pk)
    camera = itemToDelete.camera
    camera.isAvailable = 1
    camera.save()
    itemToDelete.delete()
    return redirect('viewRentalBills')