from django.shortcuts import redirect, render
from . models import SalesCamera 
from django.contrib import messages
# Create your views here.
def viewSales(request):
    pagehead = "Sales"
    object = SalesCamera.objects.all()
    return render(request,"viewSales.html",{"stocks":object,"pagehead":pagehead})


def addSales(request):
    if request.method == 'POST':
        # Extract form data from POST request
        serial_number = request.POST.get("serial_number")
        brand = request.POST.get("brand")
        model_name = request.POST.get("model_name")
        model_number = request.POST.get("model_number")
        specifications = request.POST.get("specifications")
        purchase_price = request.POST.get("purchase_price")
        photo = request.FILES.get("photo")  # Use request.FILES for file uploads
        MRp = request.POST.get("MRP")
        purchased_date = request.POST.get("purchased_date")
        type = request.POST.get("type")
        # Create a new SalesCamera instance and save it to the database
        new_stock = SalesCamera(serial_number=serial_number, brand=brand, model_name=model_name,
                                model_number=model_number, specifications=specifications,
                                purchase_price=purchase_price, photo=photo, MRP=MRp,
                                purchased_date=purchased_date, type=type)
        new_stock.save()

        messages.success(request, 'Sales data added successfully!')  # Add success message


    # Render the form template for GET requests
    pagehead = "Sales / Add Sales"
    return render(request, "addSales.html", {"pagehead": pagehead})

def editSales(request,pk):
    stockToEdit = SalesCamera.objects.get(pk=pk)
    if request.method == 'POST':
        serial_number = request.POST.get("serial_number")
        brand = request.POST.get("brand")
        model_name = request.POST.get("model_name")
        model_number = request.POST.get("model_number")
        specifications = request.POST.get("specifications")
        purchase_price = request.POST.get("purchase_price")
        photo = request.FILES.get("photo")  # Use request.FILES for file uploads
        MRp = request.POST.get("MRP")
        purchased_date = request.POST.get("purchased_date")
        type = request.POST.get("type")
        stockToEdit.serial_number=serial_number
        stockToEdit.brand=brand
        stockToEdit.model_name=model_name
        stockToEdit.model_number=model_number
        stockToEdit.specifications=specifications
        stockToEdit.purchase_price=purchase_price
        if photo is not None:
            stockToEdit.photo = photo
        stockToEdit.MRP=MRp
        stockToEdit.purchased_date=purchased_date
        stockToEdit.type=type
        stockToEdit.save()
        messages.success(request, 'Rental data updated successfully!')
        return redirect('viewSales')
    
    pagehead = "Sales / Edit Stock"
    return render(request, "EditSales.html", {"stock":stockToEdit,"pagehead": pagehead})

def deleteSales(request,pk):
    itemToDelete = SalesCamera.objects.get(pk=pk)
    itemToDelete.delete()
    pagehead = "Sales"
    object = SalesCamera.objects.all()
    return render(request,"viewSales.html",{"stocks":object,"pagehead":pagehead})
