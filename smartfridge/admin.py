from django.contrib import admin

from smartfridge.models import Product, ProductShelfDate, ListOfProduct, Images

admin.site.register(Product)
admin.site.register(ProductShelfDate)
admin.site.register(ListOfProduct)
admin.site.register(Images)

# Register your models here.
