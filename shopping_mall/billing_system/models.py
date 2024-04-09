from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

class Employee(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    # Add more fields as needed

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # Add more fields as needed
