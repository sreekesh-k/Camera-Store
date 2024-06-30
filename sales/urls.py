from django.urls import path
from . import views
#final
urlpatterns = [
    path('viewstocks/', views.viewStocks, name="viewSalesStocks"),
    path('addstock/', views.addStock, name="addSalesStock"),
    path('deletestock/<pk>', views.deleteStock, name="deleteSalesStock"),
    path('editstock/<pk>', views.editStock, name="editSalesStock"),
    path('stockdetails/<pk>', views.stockDetails,name="salesStockDetails"),
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),
]
