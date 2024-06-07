from django.urls import path
from . import views
#final
urlpatterns = [
    path('viewSales/', views.viewSales,name="viewSales"),
    path('addSales/', views.addSales,name="addSales"),
    path('deleteSales/<pk>', views.deleteSales,name="deleteSales"),
    path('editSales/<pk>', views.editSales,name="editSales"),
    path('salesDetails/<pk>', views.saleDetail,name="saleDetail"),
]
