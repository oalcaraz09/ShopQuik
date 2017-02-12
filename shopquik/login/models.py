from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=30)

class List(models.Model):
    list_name = models.CharField(max_length=30)
    items = models.ManyToManyField(Item)

class Aisle(models.Model):
    number = models.IntegerField()
    items = models.ManyToManyField(Item)

class Store(models.Model):
    store_name = models.CharField(max_length=30)
    aisles = models.ForeignKey(Aisle, on_delete=models.CASCADE)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    lists = models.ForeignKey(List, on_delete=models.CASCADE, blank=True)