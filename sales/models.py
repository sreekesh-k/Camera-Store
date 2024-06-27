from django.db import models
from django.utils import timezone

class SalesCamera(models.Model):
    CAMERA_TYPES = (
        ('camera', 'Camera'),
        ('equipment', 'Equipment')
    )
    
    serial_number = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    specifications = models.TextField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='cameraStore')
    isAvailable =models.BooleanField(default=True)
    MRP = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_date = models.DateField()
    type = models.CharField(max_length=50, choices=CAMERA_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.serial_number})"

