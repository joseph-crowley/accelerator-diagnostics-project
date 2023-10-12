from django.db import models

class Run(models.Model):
    STATUS_CHOICES = (
        ('queued', 'Queued'),
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    run_id = models.AutoField(primary_key=True)
    notes = models.TextField()
    configuration = models.ForeignKey('analysis.DiRPiConfiguration', on_delete=models.SET_NULL, null=True)
    #associated_group = models.ForeignKey('Control.DiRPiGroup', on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    
    # run-specific metadata
    num_files = models.PositiveIntegerField(default=0)
    num_events = models.PositiveIntegerField(default=0)
    livetime = models.PositiveIntegerField(default=0) # in ms
    read_deadtime = models.PositiveIntegerField(default=0) # in ms
    run_time = models.PositiveIntegerField(default=0) # in seconds
    clock_speed = models.PositiveIntegerField(default=0) # in MHz
    memory_depth = models.PositiveIntegerField(default=0) # in samples



    class Meta:
        indexes = [models.Index(fields=['run_id', 'status'])]

    def __str__(self):
        return f"Run #{self.run_id}"
