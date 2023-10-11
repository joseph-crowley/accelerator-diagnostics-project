# forms/program_form.py
from django import forms
from analysis.models import Program

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'description', 'language', 'script']

    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description'})
        self.fields['language'].widget.attrs.update({'class': 'form-control'})
        self.fields['script'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Script'})
