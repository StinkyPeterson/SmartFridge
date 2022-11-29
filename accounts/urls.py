from django.urls import path
import django.contrib.auth.views as auth_views
from accounts.views import UserCreationView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', UserCreationView.as_view(), name='sign_up'),
]