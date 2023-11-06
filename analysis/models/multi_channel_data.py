from django.db import models

class MultiChannelData(models.Model):
    record = models.ForeignKey('analysis.DataRecord', on_delete=models.CASCADE)
    channel_id = models.IntegerField()
    data_values = models.JSONField()

    class Meta:
        indexes = [models.Index(fields=['record', 'channel_id'])]
