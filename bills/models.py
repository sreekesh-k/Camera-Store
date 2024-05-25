# Create your models here.
from django.db import models
from django.utils import timezone
from sales.models import SalesCamera 

class SalesBilling(models.Model):
    camera = models.ForeignKey(SalesCamera, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phno = models.CharField(max_length=10, default='')
    customer_address = models.TextField(null=True)
    customer_email = models.EmailField(unique=True,null=True)    
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    sales_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Sales Bill - {self.id}"
