from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login

def loginview(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        success_url = reverse_lazy("whoisthis")

        ...
    else:
        # Return an 'invalid login' error message.
        ...
    success_url = reverse_lazy("homesite")

class SignUpView(CreateView):
 form_class = UserCreationForm
 success_url = reverse_lazy("login")
 template_name = "registration/signupdonor.html"