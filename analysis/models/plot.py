from django.db import models
from analysis.models.variable_choices import RUN_VAR_CHOICES, CUT_VAR_CHOICES

class Plot(models.Model):
    name = models.CharField(max_length=200, verbose_name="Plot Name")
    description = models.TextField(verbose_name="Description", blank=True)
    num_bins = models.IntegerField(verbose_name="Number of Bins")
    x_min = models.FloatField(verbose_name="X Minimum")
    x_max = models.FloatField(verbose_name="X Maximum")
    x_label = models.CharField(max_length=200, verbose_name="X Label")
    is_log_y = models.BooleanField(default=False, verbose_name="Logarithmic Y-Axis?")
    optstat = models.BooleanField(default=False, verbose_name="Stats Box?") 
    fit = models.CharField(max_length=50, blank=True, null=True, verbose_name="Fit")  # Add choices if necessary

    def __str__(self):
        return self.name

class RunData(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='runs')
    run_number = models.IntegerField(verbose_name="Run Number")
    variable = models.CharField(max_length=50, choices=RUN_VAR_CHOICES, verbose_name="Variable")
    x_scale = models.FloatField(verbose_name="X Scale")
    y_scale = models.FloatField(verbose_name="Y Scale")
    x_offset = models.FloatField(verbose_name="X Offset")
    y_offset = models.FloatField(verbose_name="Y Offset")

    def __str__(self):
        return f"RunData for Run #{self.run_number} - {self.variable}"

class Cut(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='cuts')
    cut_variable = models.CharField(max_length=50, choices=CUT_VAR_CHOICES, verbose_name="Cut Variable")
    cut_min = models.FloatField(null=True, blank=True, verbose_name="Minimum Cut Value")
    cut_max = models.FloatField(null=True, blank=True, verbose_name="Maximum Cut Value")

    def __str__(self):
        return f"Cut on {self.cut_variable}"
