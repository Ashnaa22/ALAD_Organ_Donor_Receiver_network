from django.contrib import admin
from .models import ReceiverList

# Register your models here.
class ReceiverListShow(admin.ModelAdmin):
    list_display = ['name', 'blood_group','organ_needed' ,'home_address']


admin.site.register(ReceiverList, ReceiverListShow)
