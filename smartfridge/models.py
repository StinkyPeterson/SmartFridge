from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=50)
    bar_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ListOfProduct(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    price = models.FloatField()
    date_purchase = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.id_product.name


class ProductShelfDate(models.Model):
    id_product = models.ForeignKey('Product', primary_key=True, on_delete=models.CASCADE)
    date = models.DateField()