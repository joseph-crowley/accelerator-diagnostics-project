from django.db import models

class Plot(models.Model):
    plot_id = models.AutoField(primary_key=True)
    run = models.ForeignKey('Run', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    data = models.JSONField()

    class Meta:
        indexes = [models.Index(fields=['run'])]