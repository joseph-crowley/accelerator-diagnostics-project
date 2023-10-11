# forms/workflow_form.py
from django import forms
from analysis.models import Workflow

class WorkflowForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ['name', 'description', 'programs']

    def __init__(self, *args, **kwargs):
        super(WorkflowForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['programs'].widget.attrs['class'] = 'form-control'

