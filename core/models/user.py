from enum import Enum
from django.contrib.auth.models import AbstractUser
from django.db import models

class RoleChoices(Enum):
    PUBLIC = 'Public'
    UCSB = 'UCSB'
    ADMIN = 'Admin'

class ContributorStatusChoices(Enum):
    UNDERGRAD = 'Undergraduate'
    GRADUATE = 'Graduate'
    POSTDOC = 'Postdoctoral Scholar' 
    PROFESSOR = 'Professor'
    NOT_A_CONTRIBUTOR = 'Not Applicable'

class CustomUser(AbstractUser):
    """
    Custom User model for UCSB Physics - DiRPi Project.
    """
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    role = models.CharField(
        max_length=100,
        choices=[(role.name, role.value) for role in RoleChoices if role.name != RoleChoices.ADMIN.name],
        default=RoleChoices.PUBLIC.name
    )

    contributor_status = models.CharField(
        max_length=100,
        choices=[(status.name, status.value) for status in ContributorStatusChoices],
        blank=True,
        null=True,
        default=ContributorStatusChoices.NOT_A_CONTRIBUTOR.name 
    )
