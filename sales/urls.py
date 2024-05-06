from django.urls import path
from . import views

urlpatterns = [
    path('viewSales/', views.viewSales,name="viewSales"),
    path('addSales/', views.addSales,name="addSales"),
]
