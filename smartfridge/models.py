from django.db import models

from django.contrib.auth import get_user_model

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=50)
    bar_code = models.IntegerField()


class ListOfProduct(models.Model):
    id_user = models.ForeignKey()
    id_product = models.ForeignKey()
    price = models.IntegerField()
    date_purchase = models.DateField()
    quantity = models.IntegerField()


class ProductShelfDate(models.Model):
    id_product = models.ForeignKey()