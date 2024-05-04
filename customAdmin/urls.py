from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admindash/', views.admindash, name="admindash"),
]
