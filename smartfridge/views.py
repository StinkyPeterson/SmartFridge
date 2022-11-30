from django.shortcuts import render
from django.views.generic import ListView, DetailView
from smartfridge.models import ListOfProduct, Product

def home(request):
    products = ListOfProduct.objects.all().filter(id_user = request.user.id)
    return render(request, 'home.html', {'product_list': products})

def scaner(request):
    return render(request, 'scan.html')


# Create your views here.
