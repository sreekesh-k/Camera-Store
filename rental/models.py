from django.db import models
from django.utils import timezone

class RentCamera(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    specifications = models.TextField()
    photo = models.ImageField(upload_to='images/')
    isAvailable =models.BooleanField(default=True)
    charge_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.model_number})"
