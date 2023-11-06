
from django.contrib import admin
from .models import DiRPiDevice, DiRPiGroup, DiRPiConfiguration

# Register your models here.
admin.site.register(DiRPiDevice)
admin.site.register(DiRPiGroup)
admin.site.register(DiRPiConfiguration)
