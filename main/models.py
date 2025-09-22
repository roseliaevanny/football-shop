import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('celana', 'Celana'),
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola'),
        ('aksesoris', 'Aksesoris')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def check_stock(self):
        return self.stock