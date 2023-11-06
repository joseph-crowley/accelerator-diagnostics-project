from django.db import models
from core.models import CustomUser

class DiRPiConfiguration(models.Model):
    config_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="default config")
    description = models.TextField(default="")

    # Data section
    events_per_file = models.PositiveIntegerField(default=100)
    memory_depth = models.PositiveIntegerField(default=600)

    # Trigger section
    software_trigger = models.PositiveIntegerField(default=0)
    external_trigger = models.PositiveIntegerField(default=0)
    trigger_channel1 = models.PositiveIntegerField(default=1)
    trigger_channel2 = models.PositiveIntegerField(default=1)
    prescale = models.PositiveIntegerField(choices=[(0, 'AND'), (1, 'OR')], default=1)
    trigger_position = models.PositiveIntegerField(choices=[(1, 'early'), (2, 'late')], default=2)
    dac_value_channel1 = models.PositiveIntegerField(default=250)
    dac_value_channel2 = models.PositiveIntegerField(default=250)

    # Components section
    pedestal_channel1 = models.PositiveIntegerField(default=242)
    pedestal_channel2 = models.PositiveIntegerField(default=242)
    sipm_bias_channel1 = models.PositiveIntegerField(default=56)
    sipm_bias_channel2 = models.PositiveIntegerField(default=61)
    dac_pulse_channel1 = models.PositiveIntegerField(default=0)
    dac_pulse_channel2 = models.PositiveIntegerField(default=0)
    clock_speed = models.PositiveIntegerField(default=40)

    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return "DiRPi - " + self.name