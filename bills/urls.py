from django.urls import path
from . import views

urlpatterns = [
    path('customerdetails/<pk>', views.customer,name="saleCustomer"),
    path('salesbills', views.viewSalesBills,name="viewSalesBills"),
    path('salesbills/<pk>', views.deleteSalesBills,name="deleteSalesBills"),
    path('salesbill', views.createSalesBills,name="createSalesBills"),
    path('get_cameras/',views.get_cameras,name="getcam")
]
