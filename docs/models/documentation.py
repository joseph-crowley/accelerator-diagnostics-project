# docs/models/documentation.py

from django.db import models

class Documentation(models.Model):
    DOC_TYPE_CHOICES = (
        ('guide', 'User Guide'),
        ('faq', 'FAQ'),
        ('tech', 'Technical Documentation'),
    )
    
    doc_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(choices=DOC_TYPE_CHOICES, max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
