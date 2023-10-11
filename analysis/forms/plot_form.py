# forms/plot_form.py

from django import forms
from analysis.models import Plot

class PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(PlotForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
