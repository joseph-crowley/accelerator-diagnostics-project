# models/program.py
from django.db import models
from core.models import CustomUser

class Program(models.Model):
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('root_c++', 'ROOT C++'),
    )
    program_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
    script = models.FileField(upload_to='static/scripts/')
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name + ' - ' + self.language 