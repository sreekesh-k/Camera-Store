from django.urls import path
from . import views
urlpatterns = [
    path('CustomerRentals/<pk>', views.rentcustomer,name="rentcustomer"),
    path('Rentalbills', views.viewRentalBills,name="viewRentalBills"),
    path('Rentalbills/<pk>', views.deleteRentalBills,name="deleteRentalBills"),
]
