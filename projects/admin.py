from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'start_date', 'end_date', 'status']
    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)