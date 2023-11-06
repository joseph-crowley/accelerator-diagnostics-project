from django.contrib import admin
from analysis.models import Run, DataRecord, Program, Plot, MultiChannelData

admin.site.register(Run)
admin.site.register(DataRecord)
admin.site.register(Program)
admin.site.register(Plot)
admin.site.register(MultiChannelData)
