from django.db import models
from enum import Enum

"""
DiRPi data format:
    http://dstuart.physics.ucsb.edu/Lgbk/pub/E41265.dir/E41265.html

Notes on data tiers:
    RAW = untouched, original data. Get it out asap. RPi collects, compresses, and sends
    RECO = waveform correction, pulse finding, calibration
    ANA = used for analysis
    MERGE = join from different runs or dirpis or both

See David Stuart's notes on data tiers (bottom of page): 
    http://dstuart.physics.ucsb.edu/Lgbk/pub/E41378.dir/E41378.html
"""

class DataTierChoices(Enum):
    RAW = 'RAW'
    RECO = 'RECO'
    ANA = 'ANA'
    MERGE = 'MERGE'

class DataRecord(models.Model):
    run = models.ForeignKey('analysis.Run', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    data_tier = models.CharField(max_length=255, choices=[(tier.name, tier.value) for tier in DataTierChoices], default=DataTierChoices.RAW.value)
    data_values = models.JSONField()
    anomalies = models.JSONField()

    class Meta:
        indexes = [models.Index(fields=['run', 'timestamp'])]

    def __str__(self):
        return f'{self.run} {self.timestamp}'
