from django.contrib import admin

from .models import HostingPlatform, ProjectHostingPlatform


class ProjectHostingPlatformInline(admin.TabularInline):
    model = ProjectHostingPlatform
    extra = 1


admin.site.register(HostingPlatform)
