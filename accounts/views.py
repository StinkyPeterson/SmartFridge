from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import UserSignUpForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from accounts.models import Notification

class UserCreationView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/sign_up.html'


def notification_view(request):
    notifications = Notification.objects.all().filter(id_user = request.user.id)
    return render(request, 'notifications.html', {'notifications' : notifications})

# Create your views here.
