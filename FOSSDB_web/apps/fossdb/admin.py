from django.contrib import admin

from .models import License, Project

admin.site.register(Project)
admin.site.register(License)
