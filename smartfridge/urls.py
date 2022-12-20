from django.urls import path
from smartfridge.views import home, scaner, delete_product,script

urlpatterns = [
    path('', home, name='home'),
    path('scan/', scaner, name='scaner'),
    path('delete/(?P<id>\d+)/$', delete_product, name='delete'),
    path('analiz/',script,name = 'script')

]