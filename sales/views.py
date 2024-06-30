from django.shortcuts import redirect, render
from django.http import JsonResponse
from . models import SalesCamera 
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def search_suggestions(request):
    query = request.GET.get('term', '')
    suggestions = []
    
    if query:
        cameras = SalesCamera.objects.filter(
            Q(brand__icontains=query) | 
            Q(model_name__icontains=query)
        )[:10]  # Limit the number of suggestions
    
        suggestions = [{'id': cam.id, 'label': f"{cam.brand} {cam.model_name}", 'model': cam.model_name} for cam in cameras]
    
    return JsonResponse(suggestions, safe=False)

def viewStocks(request):
    page_head = "Sales"
    query = request.GET.get('search')
    
    if query:
        stocks = SalesCamera.objects.filter(
            Q(brand__icontains=query) | 
            Q(model_name__icontains=query)
        )
    else:
        stocks = SalesCamera.objects.all()
        
    return render(request, "sales/stock/viewstocks.html", {"stocks": stocks, "pagehead": page_head})


def addStock(request):
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
    return render(request, "sales/stock/addstock.html", {"pagehead": pagehead})

def editStock(request,pk):
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
    return render(request, "sales/stock/editstock.html", {"stock":stockToEdit,"pagehead": pagehead})

def deleteStock(request,pk):
    itemToDelete = SalesCamera.objects.get(pk=pk)
    itemToDelete.delete()
    pagehead = "Sales"
    object = SalesCamera.objects.all()
    return render(request,"sales/stock/viewstock.html",{"stocks":object,"pagehead":pagehead})

def stockDetails(request,pk):
    itemToDisplay = SalesCamera.objects.get(pk=pk)
    pagehead = "Sales / Details"
    return render(request,"sales/stock/stockdetails.html",{"stock":itemToDisplay,"pagehead":pagehead})