from django.db import models
#final
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)