from django.contrib import admin

from .hosting_platform.models import HostingPlatform, ProjectHostingPlatform
from .license.models import License
from .models import Project
from .operating_system.models import OperatingSystem, OperatingSystemVersion
from .programming_language.models import ProgrammingLanguage, ProjectProgrammingLanguage
from .tag.models import Tag


class ProjectProgrammingLanguageInline(admin.TabularInline):
    model = ProjectProgrammingLanguage
    extra = 1


class ProjectHostingPlatformInline(admin.TabularInline):
    model = ProjectHostingPlatform
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectHostingPlatformInline, ProjectProgrammingLanguageInline]
    list_display = (
        "name",
        "owner",
    )

    def _languages(self, object):
        return " | ".join([i.programming_language.name for i in object.projectprogramminglanguage_set.all()])


models = (
    HostingPlatform,
    License,
    ProgrammingLanguage,
    Tag,
    OperatingSystem,
    OperatingSystemVersion,
)
for model in models:
    admin.site.register(model)

admin.site.register(Project, ProjectAdmin)
