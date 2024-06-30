from django.urls import path
from . import views

urlpatterns = [
    path('viewstocks/', views.viewStocks, name="viewRentalStocks"),
    path('addstock/', views.addStock, name="addRentalsStock"),
    path('deletestock/<pk>', views.deleteStock, name="deleteRentalStock"),
    path('editstock/<pk>', views.editStock, name="editRentalStock"),
    path('stockdetails/<pk>', views.stockDetails,name="rentalStockDetails"),
]