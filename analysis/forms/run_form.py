from django import forms
from analysis.models import Run

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ['metadata', 'configurations', 'tags', 'status']
        widgets = {
            'metadata': forms.Textarea(attrs={'placeholder': 'Enter Metadata'}),
            'configurations': forms.Textarea(attrs={'placeholder': 'Enter Configurations'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Enter Tags'}),
            'status': forms.Select(attrs={'placeholder': 'Enter Status'}),
        }
