from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True,primary_key=True,default=None)
  age = models.PositiveIntegerField(null=True, blank=True)
  is_Donor = models.BooleanField('donor status', default=False)

class Donor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True,related_name='donor')
    first_name=models.CharField(max_length=30, null=True, blank=True)
    last_name=models.CharField(max_length=30, null=True, blank=True)
    
