from django.contrib import admin

from .models import (License, ProgrammingLanguage, Project,
                     ProjectProgrammingLanguage)


class ProjectProgrammingLanguageInline(admin.TabularInline):
    model = ProjectProgrammingLanguage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectProgrammingLanguageInline]
    list_display = ("author", "name", "get_languages")

    def get_languages(self, object):
        return " | ".join([i.language.language for i in object.projectprogramminglanguage_set.all()])


admin.site.register(License)
admin.site.register(ProgrammingLanguage)
admin.site.register(Project, ProjectAdmin)
# admin.site.register(HostingPlatform)
