from email import message
from django.db import models
from django.forms import CharField

# Create your models here.
class Inquiry(models.Model):
    fullname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=32)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)