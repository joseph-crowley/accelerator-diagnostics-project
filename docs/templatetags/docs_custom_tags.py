from django import template
from django.utils import timezone
from datetime import datetime
from docs.models import Documentation

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

# Get Documentation by Type
@register.filter
def get_docs_by_type(type):
    return Documentation.objects.filter(type=type)

# Get Documentation by ID
@register.filter
def get_docs_by_id(doc_id):
    return Documentation.objects.get(doc_id=doc_id)

# Get Documentation by Title
@register.filter
def get_docs_by_title(title):
    return Documentation.objects.get(title=title)
