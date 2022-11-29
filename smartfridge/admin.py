from django.contrib import admin

from smartfridge.models import Product, ProductShelfDate, ListOfProduct

admin.site.register(Product)
admin.site.register(ProductShelfDate)
admin.site.register(ListOfProduct)

# Register your models here.
