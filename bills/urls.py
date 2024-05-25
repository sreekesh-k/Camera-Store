from django.urls import path
from . import views

urlpatterns = [
    path('Customer/<pk>', views.customer,name="customer"),
    path('bills', views.viewSalesBills,name="viewSalesBills"),
    path('bills/<pk>', views.deleteSalesBills,name="deleteSalesBills"),
]
