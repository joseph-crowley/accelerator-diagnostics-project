from django.db import models

class Run(models.Model):
    STATUS_CHOICES = (
        ('queued', 'Queued'),
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    run_id = models.AutoField(primary_key=True)
    metadata = models.TextField()
    configurations = models.TextField()
    #associated_group = models.ForeignKey('Control.DiRPiGroup', on_delete=models.CASCADE, null=True)
    tags = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)

    class Meta:
        indexes = [models.Index(fields=['run_id', 'status'])]

    def __str__(self):
        return f"Run #{self.run_id}"
