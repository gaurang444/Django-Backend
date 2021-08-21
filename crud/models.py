from django.db import models
from django.utils import timezone

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class User(models.Model):
    user_name = models.CharField(max_length=255, null=True, blank=True)
    adhar_num=  models.CharField(max_length=255, null=True, blank=True)
    phone_num=  models.CharField(max_length=255, null=True, blank=True)
    email=      models.CharField(max_length=255, null=True, blank=True)
    address=    models.CharField(max_length=255, null=True, blank=True)
    is_Active=  models.BooleanField(blank=True, null=True, default=True)  #soft deletion user 
    user_created_at=models.DateTimeField(default=timezone.now)
    last_updatedat=AutoDateTimeField(default=timezone.now)
    
