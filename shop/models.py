from django.db import models


class UserCreate(models.Model):
    username = models.CharField(max_length=128,unique=True)
    password = models.CharField()

class Product(models.Model):

    CATEGORY_CHOICES = [
    ('fruits', 'Fruits & Vegetables'),
    ('meat', 'Meat & Poultry'),
    ('dairy', 'Dairy Products'),
    ('bakery', 'Bakery & Sweets'),
    ('drinks', 'Beverages'),
    ]

    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128,choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Product(id={self.id}, name="{self.name}")'
    
class Shoping(models.Model):

    CATEGORY_CHOICES = [
    ('fruits', 'Fruits & Vegetables'),
    ('meat', 'Meat & Poultry'),
    ('dairy', 'Dairy Products'),
    ('bakery', 'Bakery & Sweets'),
    ('drinks', 'Beverages'),
    ]

    username = models.ForeignKey(to=UserCreate,on_delete=models.CASCADE,related_name='product')
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128,choices=CATEGORY_CHOICES)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f'Product(id={self.id}, name="{self.name}")'
    
