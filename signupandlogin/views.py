from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationFormDonor

class SignUpViewDonor(CreateView):
 form_class = CustomUserCreationFormDonor
 success_url = reverse_lazy('home')
 template_name = "signupdonor.html"