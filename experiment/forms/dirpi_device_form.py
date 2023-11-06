
from django import forms
from experiment.models import DiRPiDevice

# Form to facilitate user input for DiRPiDevice
class DiRPiDeviceForm(forms.ModelForm):
    # Unique identifier for the DiRPi Device
    device_number = forms.IntegerField()
    
    # Configurations for the DiRPi Device
    configurations = forms.JSONField()
    
    # Status of the DiRPi Device
    status = forms.CharField(max_length=50)
    
    class Meta:
        model = DiRPiDevice
        fields = ['device_number', 'configurations', 'status']
