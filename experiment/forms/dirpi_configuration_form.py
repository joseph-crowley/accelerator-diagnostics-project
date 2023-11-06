from django import forms
from experiment.models import DiRPiConfiguration

class DiRPiConfigurationForm(forms.ModelForm):
    
    class Meta:
        model = DiRPiConfiguration
        fields = [
            'name', 
            'description',
            'events_per_file',
            'memory_depth',
            'software_trigger',
            'external_trigger',
            'trigger_channel1',
            'trigger_channel2',
            'prescale',
            'trigger_position',
            'dac_value_channel1',
            'dac_value_channel2',
            'pedestal_channel1',
            'pedestal_channel2',
            'sipm_bias_channel1',
            'sipm_bias_channel2',
            'dac_pulse_channel1',
            'dac_pulse_channel2',
            'clock_speed'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'events_per_file': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'memory_depth': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'prescale': forms.Select(choices=[(0, 'AND'), (1, 'OR')], attrs={'class': 'form-control'}),
            'trigger_position': forms.Select(choices=[(1, 'early'), (2, 'late')], attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # For other fields not explicitly set in the Meta class:
        for field in self.fields:
            if not self.fields[field].widget.attrs.get('class'):
                self.fields[field].widget.attrs.update({'class': 'form-control'})

        # TODO: For specific constraints on certain fields, add them here. 
        # Example: Limiting DAC values based on the provided config:
        #self.fields['dac_value_channel1'].widget.attrs.update({'min': 0, 'max': 400})
        #self.fields['dac_value_channel2'].widget.attrs.update({'min': 0, 'max': 400})

    def clean_memory_depth(self):
        memory_depth = self.cleaned_data.get('memory_depth')
        if memory_depth < 1 or memory_depth > 1000:
            raise forms.ValidationError('Memory depth must be between 1 and 1000.')
        return memory_depth
