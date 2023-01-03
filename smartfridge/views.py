import json
import datetime

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from smartfridge.models import ListOfProduct, Product
from smartfridge.forms import ScanForm
from django.contrib.auth.models import User
import requests
from accounts.models import Notification

def home(request):
    products = ListOfProduct.objects.all().filter(id_user = request.user.id, in_fridge = True)
    return render(request, 'home.html', {'product_list': products})

def scaner(request):
    if request.method == 'GET':
        form = ScanForm()
        return render(request, 'scan.html', {"form" : form})
    if request.method == 'POST':
        form = ScanForm(request.POST)
        if form.is_valid():
            r = request_check(form) #запрос через API проверка чека
            data = json.loads(r.text) #получение чека 
            # print(r.text)
            products = data['data']['json']['items'] #получение списка продуктов
            date = data['data']['json']['dateTime'].split('T')[0] #получение даты покупки 
            insert_products(products, request,date) #добавление продуктов в БД
            script(request)
            return redirect('scaner')




def insert_products(products, request,date):
    for product in products:
        print(product['name'])
        new_product = Product()
        new_product.name = product['name']
        # new_product.product_type = str(product['productType'])
        new_product.bar_code = 0
        product_db = Product.objects.all().filter(name=new_product.name)
        if not product_db:
            new_product.save()
        product_in_fridge = ListOfProduct()
        product_in_fridge.id_user = request.user
        if product_db:
            product_in_fridge.id_product = Product.objects.all().get(name=new_product.name)
        else:
            product_in_fridge.id_product = new_product
        product_in_fridge.price = int(product['sum']) / 100
        product_in_fridge.quantity = int(product['quantity'])
        product_in_fridge.date_purchase = date
        product_in_fridge.in_fridge = True
        if product_db:
            try:
                product_in_fridge_db = ListOfProduct.objects.get(id_user=request.user.id,
                                                             id_product=Product.objects.get(name=new_product.name,
                                                                                            ), date_purchase = date)
            except:
                product_in_fridge_db = None
            if product_in_fridge_db:
                product_in_fridge_db.quantity += product_in_fridge.quantity
                product_in_fridge_db.save(update_fields=['quantity'])
            else:
                product_in_fridge.save()
        else:
            product_in_fridge.save()
    # print(data['data']['json']['items'])



def request_check(form):
    data = form.data
    url = 'https://proverkacheka.com/api/v1/check/get'
    token = 'INPUT YOUR TOKEN HERE'
    data = {
        'token': token,
        'qrraw': data.get('qrcode_string')
    }
    r = requests.post(url, data=data)
    return r


def delete_product(request, id):
    product = ListOfProduct.objects.get(id = id)
    product.quantity -= 1
    if product.quantity <= 0:
        product.in_fridge = False
        product.save()
    else:
        product.save(update_fields=['quantity'])

    return redirect('home')


def script(request):
    users = User.objects.all()
    #print(users[0])
    for user in users:
        products = ListOfProduct.objects.all().filter(id_user=user)
        diction_product = {}
        for product in products:
            if product.id_product.name in diction_product:
                diction_product[product.id_product.name]+=1
            else:
                diction_product[product.id_product.name] = 1
        print(diction_product)
        for product in diction_product:
            if diction_product[product]>2:
                products_analiz = ListOfProduct.objects.all().filter(id_user=user,id_product=Product.objects.get(name = product))
                slice_product = products_analiz[1:]
                for product_anal in products_analiz:
                    print(product_anal.date_purchase)
                slice_product_post = slice_product[0].date_purchase
                slice_product_now = slice_product[1].date_purchase
                slice_product_finish = (slice_product_now-slice_product_post)
                notific = Notification(id_user = user,message = f'У вас может закончится {Product.objects.get(name = product)} докупите его',date = slice_product_now + slice_product_finish)
                try:
                    notific_db = Notification.objects.get(id_user = notific.id_user, message = notific.message, date = notific.date)
                except:
                    notific_db = None
                if not notific_db:
                    notific.save()

    #return redirect("home")
# Create your views here.
