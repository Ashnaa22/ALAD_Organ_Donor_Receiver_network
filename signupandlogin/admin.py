from django.contrib import admin
from .forms import CustomUserCreationFormDonor,UserCreationForm
from .models import CustomUser,Donor

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Donor)