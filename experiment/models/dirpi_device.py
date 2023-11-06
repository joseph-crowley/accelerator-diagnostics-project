import uuid
from django.db import models

# Model to represent a DiRPi Device
class DiRPiDevice(models.Model):
    # Unique identifier for the DiRPi Device
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Group to which this DiRPi Device belongs
    group = models.ForeignKey('experiment.DiRPiGroup', related_name='devices', on_delete=models.CASCADE)  

    # diRPi Device number
    device_number = models.IntegerField()
    
    # IP Address of the DiRPi Device
    device_ip = models.CharField(max_length=255)

    # Configurations for the DiRPi Device
    configuration = models.ForeignKey('experiment.DiRPiConfiguration', on_delete=models.CASCADE)
    
    # Status of the DiRPi Device
    status = models.CharField(max_length=50)
    
    # Last time the DiRPi Device sent a ping
    last_ping_time = models.DateTimeField()
    
    # Health status of the DiRPi Device
    health_status = models.CharField(max_length=50)

    # Current run number of the DiRPi Device
    current_run_number = models.IntegerField()
