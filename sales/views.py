from django.shortcuts import render
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
    pagehead = "Add Sales"
    return render(request, "addSales.html", {"pagehead": pagehead})