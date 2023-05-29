from django import forms


class DonorSearch(forms.Form):
    

    organ_s_choice = (
        ("all" , "All"),
        ("kidney" , "Kidney"),
        ("lung" , "Lung"),
        ("liver" , "Liver"),
        ("pancreas" , "Pancreas"),
        ("intestine" , "Intestine"),
        ("eye" , "Eye"),
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
    

