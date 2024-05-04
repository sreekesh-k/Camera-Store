from django.db import models
from rental.models import RentCamera 
from django.utils import timezone

class RentalBilling(models.Model):
    camera = models.ForeignKey(RentCamera, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Sales Bill - {self.id}"
