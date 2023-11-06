
from django import forms
from experiment.models import DiRPiGroup

# Form to facilitate user input for DiRPiGroup
class DiRPiGroupForm(forms.ModelForm):
    # Name of the DiRPi Group
    group_name = forms.CharField(max_length=255)
    
    # Location of the DiRPi Group
    location = forms.CharField(max_length=255)
    
    # Password to access the DiRPi Group
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    
    class Meta:
        model = DiRPiGroup
        fields = ['group_name', 'location', 'password']
