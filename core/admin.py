# core/admin.py

from django.contrib import admin

# Site-wide settings
from .models.user import CustomUser
admin.site.register(CustomUser)

# Team members - Project Admin and Faculty Sponsor
from .models.team import TeamMember
admin.site.register(TeamMember)
