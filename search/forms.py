from django import forms


class DonorSearch(forms.Form):
    

    organ_s_choice = (
        ("one_kidney" , "One_Kidney"),
        ("a_Single_lob_from_lung" , "A_Single_lob_from_lung"),
        ("a_portion_of_liver" , "A_portion_of_liver"),
        ("a_portion_of_pancreas" , "A_portion_of_Pancreas"),
        ("a_portion_of_intestine" , "A_portion_of_intestine"),
    )

    select_organ = forms.ChoiceField(
        choices=organ_s_choice,
        widget=forms.Select(
            attrs={'class':'form-control',
            'required':'True',
            },
            ),
    )

    select_location = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control',
            'required':'True', 
            'placeholder':'where do you need?. e.g. dhaka'
            }
        ),
    )
    

