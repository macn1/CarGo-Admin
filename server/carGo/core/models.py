from django.db import models

class Car (models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    year = models.PositiveBigIntegerField()

class Expense(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True, blank=True, related_name='expenses')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
class Income(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.SET_NULL,  # Don't delete income if car is deleted
        null=True,               
        blank=True,                
        related_name='incomes'
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)