from django.db import models
from dreg.models import DonorList
from .views import reqdetailsave

class reqdetails(models.Model):
    donor_email=models.EmailField(blank=True, null=True,)
    receiver_email=models.EmailField(blank=True, null=True,)