from django.urls import path
from smartfridge.views import home, scaner

urlpatterns = [
    path('', home, name='home'),
    path('/scan', scaner, name='scaner')

]