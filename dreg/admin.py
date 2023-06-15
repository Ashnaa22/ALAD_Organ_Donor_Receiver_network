from django.contrib import admin
from .models import DonorList


class DonorListShow(admin.ModelAdmin):
    list_display = ['user_name','name', 'blood_group','organ' ,'home_address']


admin.site.register(DonorList, DonorListShow)
