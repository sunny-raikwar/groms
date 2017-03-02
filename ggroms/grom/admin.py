from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.StaffUser)
admin.site.register(models.LandDetail)
admin.site.register(models.AgentAccount)
admin.site.register(models.AgentType)
admin.site.register(models.NominiDetail)
admin.site.register(models.AgentDetail)
admin.site.register(models.CustomerDetail)
admin.site.register(models.ProjectDetail)
admin.site.register(models.LayoutDetail)
admin.site.register(models.PlotDetail)
