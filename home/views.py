from django.shortcuts import render
from .models import HomePageBody



def homedisplay(request):
    our_vision = HomePageBody.objects.get(id_vision=1)
    donor_opinion = HomePageBody.objects.get(id_vision=2)
    receiver_opinion = HomePageBody.objects.get(id_vision=3)
    
    

    context = {
        
        'our_vision' : our_vision,
        'donor_opinion' : donor_opinion,
        'receiver_opinion' : receiver_opinion,
    }

    return render(request, 'donor_home.html', context)


