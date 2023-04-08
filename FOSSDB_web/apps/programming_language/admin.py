from django.contrib import admin

from .models import ProgrammingLanguage, ProjectProgrammingLanguage


class ProjectProgrammingLanguageInline(admin.TabularInline):
    model = ProjectProgrammingLanguage
    extra = 1


admin.site.register(ProgrammingLanguage)
