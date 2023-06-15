from django.urls import path
from .views import whoselect

urlpatterns = [
 path('', whoselect, name="whoisthis"),
]
