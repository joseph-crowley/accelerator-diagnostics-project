from django import forms
from analysis.models import Run
from experiment.models import DiRPiConfiguration

class DataFilterForm(forms.Form):
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    tags = forms.CharField(required=False)
    status = forms.CharField(required=False)
    run = forms.ModelChoiceField(queryset=Run.objects.all(), required=False)
    group_id = forms.IntegerField(required=False)
    dirpi_configurations = forms.ModelMultipleChoiceField(queryset=DiRPiConfiguration.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(DataFilterForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Start Date'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'End Date'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tags'})
        self.fields['status'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Status'})
        self.fields['run'].widget.attrs.update({'class': 'form-control'})
        self.fields['group_id'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Group ID'})
        self.fields['dirpi_configurations'].widget.attrs.update({'class': 'form-control'})

