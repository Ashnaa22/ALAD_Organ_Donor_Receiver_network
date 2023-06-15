from django.shortcuts import render
from search.forms import DonorSearch
from dreg.models import DonorList
# Create your views here.


def reqdetailsave(request,email):
    email=email
    detail=DonorList()
    detail=DonorList.objects.get(email=email)
    context = {
        'details' : detail
    }