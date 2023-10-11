from django.db import models

class DataRecord(models.Model):
    run = models.ForeignKey('Run', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    data_values = models.JSONField()
    anomalies = models.JSONField()

    class Meta:
        indexes = [models.Index(fields=['run', 'timestamp'])]
