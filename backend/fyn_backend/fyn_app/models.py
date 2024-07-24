from django.db import models

class Component(models.Model):
    user = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    new_purchase_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()


class Issue(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.TextField()
    component = models.ForeignKey(Component, on_delete=models.SET_NULL, null=True, blank=True)
    is_new_component = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Transaction(models.Model):
    pass



