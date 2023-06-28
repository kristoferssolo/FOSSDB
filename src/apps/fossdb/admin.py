from django.contrib import admin

from .models import (
    HostingPlatform,
    License,
    OperatingSystem,
    OperatingSystemVersion,
    ProgrammingLanguage,
    Project,
    ProjectHostingPlatform,
    ProjectProgrammingLanguage,
    Tag,
)


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
