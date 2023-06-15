from django.db import models
from django.contrib.auth.models import User

#Receiverresistration forms data table
class ReceiverList(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receiver_lists',unique=True)   

    name = models.CharField(max_length = 50, blank=True, null=True)
    
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
    ]
    gender = models.CharField(
        max_length=6, blank=True, null=True,
        choices=gender_choices,
        )
    date_of_birth = models.DateField(blank=True, null=True)

    organ_choices=[
        ("heart" , "Heart"),
        ("kidney" , "Kidney"),
        ("lung" , "Lung"),
        ("liver" , "Liver"),
        ("pancreas" , "Pancreas"),
        ("intestine" , "Intestine"),
        ("eye" , "Eye"),
    ]
    organ_needed= models.CharField(
        max_length=20, blank=True, null=True,
        choices=organ_choices
        )
    blood_choices=[
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),

    ]
    blood_group = models.CharField(
        max_length=4, blank=True, null=True,
        choices=blood_choices
        )
    emergency_contact_name = models.CharField(max_length = 50, blank=True, null=True)
    emergency_contact_number= models.IntegerField(blank=True, null=True)
    id_choices=[
        ('pancard',"Pancard"),
        ("adhaarcard","Aadhaarcard"),
        ("voterid","Voterid"),
    ]
    choose_identity_card=models.CharField(
        max_length=10, blank=True, null=True,
        choices=id_choices
        )
    enter_identity_card_number = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    occupation = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    last_donate_date = models.CharField(max_length=50, blank=True, null=True)
    any_diseases_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    any_diseases = models.CharField(
        max_length=4, blank=True, null=True,
        choices=any_diseases_choices,
        )
    allergies_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    allergies = models.CharField(
        max_length=4, blank=True, null=True,
        choices=allergies_choices,
        )
    cardiac_choices=[
        ("yes","Yes"),
        ("no", "No"),
    ]
    cardiac = models.CharField(
        max_length=4, blank=True, null=True,
        choices=cardiac_choices,
        )
    bleeding_disorders_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    bleeding_disorders = models.CharField(
        max_length=4, blank=True, null=True,
        choices=bleeding_disorders_choices,
        )
    hbsAg_hcv_hIV_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    hbsAg_hcv_hIV =models.CharField(
        max_length=4, blank=True, null=True,
        choices=hbsAg_hcv_hIV_choices,
        )



    def __str__(self):
        return self.name



