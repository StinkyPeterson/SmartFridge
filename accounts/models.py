from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    date = models.DateField(blank=True)