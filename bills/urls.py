from django.urls import path
from . import views

urlpatterns = [
    path('Customer/<pk>', views.customer,name="customer"),
    
]
