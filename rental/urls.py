from django.urls import path
from . import views

urlpatterns = [
    path('viewRentals/', views.viewRentals, name="viewRentals"),
    path('addRentals/', views.addRentals, name="addRentals"),
    path('deleteRentals/<pk>', views.deleteRentals, name="deleteRentals"),
    path('editRentals/<pk>', views.editRentals, name="editRentals"),
]