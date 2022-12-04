import json
import datetime

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from smartfridge.models import ListOfProduct, Product
from smartfridge.forms import ScanForm
import requests

def home(request):
    products = ListOfProduct.objects.all().filter(id_user = request.user.id)
    return render(request, 'home.html', {'product_list': products})

def scaner(request):
    t = "20221115T2244 & s = 135.87 & fn = 9960440301659302 & i = 86567 & fp = 1068132758 & n = 1"
    if request.method == 'GET':
        form = ScanForm()
        return render(request, 'scan.html', {"form" : form})
    if request.method == 'POST':
        form = ScanForm(request.POST)
        if form.is_valid():
            r = request_check(form)
            data = json.loads(r.text)
            products = data['data']['json']['items']
            insert_products(products, request)
            return redirect('scaner')



def insert_products(products, request):
    for product in products:
        print(product['name'])
        new_product = Product()
        new_product.name = product['name']
        new_product.product_type = str(product['productType'])
        new_product.bar_code = 0
        product_db = Product.objects.all().filter(name=new_product.name)
        if not product_db:
            new_product.save()
        product_in_fridge = ListOfProduct()
        product_in_fridge.id_user = request.user
        if product_db:
            print(type(Product.objects.get(name=new_product.name, product_type=new_product.product_type)))
            product_in_fridge.id_product = Product.objects.all().get(name=new_product.name,
                                                                     product_type=new_product.product_type)
        else:
            product_in_fridge.id_product = new_product
        product_in_fridge.price = int(product['sum']) / 100
        product_in_fridge.quantity = int(product['quantity'])
        product_in_fridge.date_purchase = datetime.date.today()
        if product_db:
            product_in_fridge_db = ListOfProduct.objects.get(id_user=request.user.id,
                                                             id_product=Product.objects.get(name=new_product.name,
                                                                                            product_type=new_product.product_type))
            if product_in_fridge_db:
                product_in_fridge_db.quantity += product_in_fridge.quantity
                product_in_fridge_db.save(update_fields=['quantity'])
        else:
            product_in_fridge.save()
    # print(data['data']['json']['items'])



def request_check(form):
    data = form.data
    url = 'https://proverkacheka.com/api/v1/check/get'
    token = '17639.WgFbE0Usn2HhAGg8e'
    data = {
        'token': token,
        'qrraw': data.get('qrcode_string')
    }
    r = requests.post(url, data=data)
    return r

# Create your views here.
