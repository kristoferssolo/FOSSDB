from django.contrib import admin

from .models import (HostingPlatform, License, ProgrammingLanguage, Project,
                     ProjectHostingPlatform, ProjectProgrammingLanguage, Tag)


class ProjectProgrammingLanguageInline(admin.TabularInline):
    model = ProjectProgrammingLanguage
    extra = 1


class ProjectHostingPlatformInline(admin.TabularInline):
    model = ProjectHostingPlatform
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectProgrammingLanguageInline, ProjectHostingPlatformInline]
    list_display = ("author", "name", "_languages", "_hosting_platform")

    def _languages(self, object):
        return " | ".join([i.language.language for i in object.projectprogramminglanguage_set.all()])

    def _hosting_platform(self, object):
        return " | ".join([i.hosting_platform.hosting_platform for i in object.projecthostingplatform_set.all()])


admin.site.register(License)
admin.site.register(ProgrammingLanguage)
admin.site.register(HostingPlatform)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
