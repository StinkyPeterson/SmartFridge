from django.urls import path
from smartfridge.views import home

urlpatterns = [
    path('', home, name='home')
]