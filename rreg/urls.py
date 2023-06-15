from django.urls import path
from .views import receiverregdisplay
#, donorregsuccess

urlpatterns = [
    path('', receiverregdisplay, name='rregsite'),
    path('receivers', receiverregdisplay, name='rregdisplay')
    
]