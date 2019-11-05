from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return 'Company: {} - Value: {}'.format(company, value)

class Recharge(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    value = models.IntegerField()
    created_at = models.DateTimeField('created at')

    def __str__(self):
        return 