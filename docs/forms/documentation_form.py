# docs/forms/documentation_form.py

from django import forms
from docs.models import Documentation

class DocumentationForm(forms.ModelForm):
    class Meta:
        model = Documentation
        fields = ['title', 'content', 'type']
