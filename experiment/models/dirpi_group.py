
from django.db import models
from core.models import CustomUser as User

# Model to represent a DiRPi Group
class DiRPiGroup(models.Model):
    # Name of the DiRPi Group
    group_name = models.CharField(max_length=255)
    
    # Location of the DiRPi Group
    location = models.CharField(max_length=255)
    
    # Password to access the DiRPi Group
    password = models.CharField(max_length=255)
    
    # Users associated with this DiRPi Group
    associated_users = models.ManyToManyField(User)
    
    # Health status of the DiRPi Group
    health_status = models.CharField(max_length=50)