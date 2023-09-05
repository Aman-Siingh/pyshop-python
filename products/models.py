from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models. CharField(max_length=2083)


class Offer(models.Model):
    code = models.TextField(max_length=10)
    description = models.TextField(max_length=250)
    discount = models.FloatField()
