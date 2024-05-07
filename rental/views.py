from django.shortcuts import render, redirect
from .models import RentCamera
from django.contrib import messages

def viewRentals(request):
    pagehead = "Rentals"
    objects = RentCamera.objects.all()
    return render(request, "viewRentals.html", {"stocks": objects, "pagehead": pagehead})

def addRentals(request):
    if request.method == 'POST':
        brand = request.POST.get("brand")
        model_name = request.POST.get("model_name")
        model_number = request.POST.get("model_number")
        specifications = request.POST.get("specifications")
        charge_per_day = request.POST.get("charge_per_day")
        photo = request.FILES.get("photo")  # Use request.FILES for file uploads
        # Extract form data from POST request
        new_stock = RentCamera(brand=brand, model_name=model_name,
                                model_number=model_number, specifications=specifications,
                                charge_per_day=charge_per_day, photo=photo)
        new_stock.save()
        messages.success(request, 'Rental data added successfully!')

    pagehead = "Add Rentals"
    return render(request, "addRentals.html", {"pagehead": pagehead})

def editRentals(request, pk):
    stockToEdit = RentCamera.objects.get(pk=pk)
    if request.method == 'POST':
        brand = request.POST.get("brand")
        model_name = request.POST.get("model_name")
        model_number = request.POST.get("model_number")
        specifications = request.POST.get("specifications")
        charge_per_day = request.POST.get("charge_per_day")
        photo = request.FILES.get("photo")  # Use request.FILES for file uploads
        stockToEdit.brand = brand
        stockToEdit.model_name = model_name
        stockToEdit.model_number = model_number
        stockToEdit.specifications = specifications
        stockToEdit.charge_per_day = charge_per_day
        if photo:
            stockToEdit.photo = photo
        stockToEdit.save()
        messages.success(request, 'Rental data updated successfully!')
        return redirect('view_rentals')

    pagehead = "Edit Rental"
    return render(request, "EditRentals.html", {"stock": stockToEdit, "pagehead": pagehead})

def deleteRentals(request, pk):
    itemToDelete = RentCamera.objects.get(pk=pk)
    itemToDelete.delete()
    messages.success(request, 'Rental data deleted successfully!')
    pagehead = "Rentals"
    objects = RentCamera.objects.all()
    return render(request, "viewRentals.html", {"stocks": objects, "pagehead": pagehead})