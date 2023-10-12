from django import forms
from analysis.models import Run

class RunForm(forms.ModelForm):
    
    class Meta:
        model = Run
        fields = [
            'notes',
            'configuration',
            'status',
            'num_files',
            'num_events',
            'livetime',
            'read_deadtime',
            'run_time',
            'clock_speed',
            'memory_depth'
        ]
        
        widgets = {
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'configuration': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=Run.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'num_files': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'num_events': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'livetime': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'read_deadtime': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'run_time': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'clock_speed': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'memory_depth': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # For any additional styling or attributes
        for field in self.fields:
            if not self.fields[field].widget.attrs.get('class'):
                self.fields[field].widget.attrs.update({'class': 'form-control'})
