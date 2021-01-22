from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


from django.db import models

class AirplaneCollector(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    jwt_token = models.CharField(max_length=500, default='', blank=True)