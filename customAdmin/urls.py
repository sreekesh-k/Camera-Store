from django.urls import path
from . import views

#final
urlpatterns = [
    path('', views.login, name="login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admindash/', views.admindash, name="admindash"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
]
