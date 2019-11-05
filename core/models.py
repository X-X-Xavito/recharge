from django.db import models
from rest_framework import routers, serializers, viewsets

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return 'Company: {}'.format(self.name)

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return 'Product: {} - Value: {}'.format(self.company, self.value)

class Recharge(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    value = models.IntegerField()
    created_at = models.DateTimeField('created at')

    def __str__(self):
        return 'Recharge ID: {}'.format(self.id)