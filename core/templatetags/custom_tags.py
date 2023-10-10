from django import template
from django.utils import timezone
from datetime import datetime
from core.models.user import CustomUser

register = template.Library()

# User Role Label
@register.filter
def user_role_label(CustomUser):
    if CustomUser.role == 'admin':
        return 'Admin'
    elif CustomUser.role == 'member':
        return 'Member'
    else:
        return 'Unknown'

# Format Date as Month Day, Year
@register.filter
def format_date(date):
    return datetime.strftime(date, '%B %d, %Y')
