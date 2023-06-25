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


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectProgrammingLanguageInline]
    list_display = ("name", "author", "_languages", "hosting_platform")

    def _languages(self, object):
        return " | ".join(
            [i.language.name for i in object.projectprogramminglanguage_set.all()]
        )


models = (
    HostingPlatform,
    # ProjectHostingPlatform,  # WARNING: remove this
    License,
    ProgrammingLanguage,
    Tag,
    OperatingSystem,
    OperatingSystemVersion,
)
for model in models:
    admin.site.register(model)

admin.site.register(Project, ProjectAdmin)
