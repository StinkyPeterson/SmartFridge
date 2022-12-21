from smartfridge.models import Product, ProductShelfDate, ListOfProduct
from django.contrib.auth.models import User
def script():
    users = User.objects.all()
    print(users)