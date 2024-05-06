from django.urls import path
from . import views

urlpatterns = [
    path('addSales/', views.addSales,name="addSales"),
]
