from django.db import models

class TeamMember(models.Model):
    # Fields
    name = models.CharField(max_length=255, verbose_name="Name")
    contact_info = models.CharField(max_length=255, verbose_name="Contact Information")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='static/images/team_members', null=True, blank=True, verbose_name="Profile Image")
    
    # Metadata
    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['name']  # orders team members alphabetically by default

    # Methods
    def __str__(self):
        return self.name
    