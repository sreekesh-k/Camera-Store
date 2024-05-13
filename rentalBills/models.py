from django.db import models
from rental.models import RentCamera 
from django.utils import timezone

class RentalBilling(models.Model):
    camera = models.ForeignKey(RentCamera, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phno = models.CharField(max_length=10, default='')
    customer_address = models.TextField(null=True)
    customer_email = models.EmailField(unique=True,null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Sales Bill - {self.id}"
