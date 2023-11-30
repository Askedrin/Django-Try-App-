from django.db import models

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
