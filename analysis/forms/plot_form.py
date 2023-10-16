from django import forms
from django.forms import inlineformset_factory
from analysis.models import Plot, RunData, Cut

class PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = [
            'name', 'description', 'num_bins', 'x_min', 'x_max', 'x_label', 'fit', 'is_log_y', 'optstat'
        ]
        
    def __init__(self, *args, **kwargs):
        super(PlotForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        # add boolean fields to this list if you want to use the default checkbox widget
        boolean_fields = [
            'is_log_y', 'optstat'
        ]

        for field in boolean_fields:
            self.fields[field].widget.attrs['class'] = 'form-check-input'

RunDataFormSet = inlineformset_factory(
    Plot, RunData,
    fields=('run_number', 'variable', 'x_scale', 'y_scale', 'x_offset', 'y_offset'),
    extra=1,
    widgets={
        'run_number': forms.NumberInput(attrs={'class': 'form-control'}),
        'variable': forms.Select(attrs={'class': 'form-control'}),
        'x_scale': forms.NumberInput(attrs={'class': 'form-control'}),
        'y_scale': forms.NumberInput(attrs={'class': 'form-control'}),
        'x_offset': forms.NumberInput(attrs={'class': 'form-control'}),
        'y_offset': forms.NumberInput(attrs={'class': 'form-control'}),
    },
    exclude=('id', 'plot'),
    can_delete=False,  # False if you don't want the delete checkbox
)

CutFormSet = inlineformset_factory(
    Plot, Cut,
    fields=('cut_variable', 'cut_min', 'cut_max'),
    extra=1,
    widgets={
        'cut_variable': forms.Select(attrs={'class': 'form-control'}),
        'cut_min': forms.NumberInput(attrs={'class': 'form-control'}),
        'cut_max': forms.NumberInput(attrs={'class': 'form-control'}),
    },
    exclude=('id', 'plot'),
    can_delete=False,  # False if you don't want the delete checkbox
)
