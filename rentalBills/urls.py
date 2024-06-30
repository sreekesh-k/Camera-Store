from django.urls import path
from . import views
urlpatterns = [
    path('customerDetails/<pk>', views.rentcustomer,name="rentcustomer"),
    path('Rentalbills', views.viewRentalBills,name="viewRentalBills"),
    path('Rentalbills/<pk>', views.deleteRentalBill,name="deleteRentalBill"),
    path('Rentalbill', views.createRentalBills,name="createRentalBills"),
]
