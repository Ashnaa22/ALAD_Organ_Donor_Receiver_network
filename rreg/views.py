from django.shortcuts import render
from django.shortcuts import render
from .forms import ReceiverRegistration
from .models import ReceiverList


#Receiver forms display
def receiverregdisplay(request):
    forms = ReceiverRegistration()
    if request.method == 'POST':
        forms = ReceiverRegistration(request.POST)
        if forms.is_valid():
            forms.save()
            print(forms.errors)
            context_details ={
                'forms' : forms
            }
            #After receiver registation donor details display
            return render(request, 'donor_reg_s.html', context_details)
            

    context = {
                'forms' : forms,
            }


    return render(request, 'receiver_reg.html', context)


