from enum import unique
from django import forms
from django.forms import ModelForm
from .models import ReceiverList
    
    
#Receiver registrarion forms create
class ReceiverRegistration(ModelForm):
    class Meta:
        model = ReceiverList
        fields = '__all__'
        widgets = {

            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'blood_group' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'organ_needed' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'emergency_contact_name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'emergency_contact_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'choose_identity_card' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'enter_identity_card_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'home_address' : forms.Textarea(attrs={'class':'form-control', 'required':'True'}),
            'last_donate_date' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'any_diseases' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'allergies' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'cardiac' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'bleeding_disorders' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'hbsAg_hcv_hIV' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            
        }