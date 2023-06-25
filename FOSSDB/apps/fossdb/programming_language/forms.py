from django import forms
from django.forms import inlineformset_factory
from fossdb.models import Project

from .models import ProgrammingLanguage, ProjectProgrammingLanguage


class ProgrammingLanguageForm(forms.ModelForm):
    programming_language = forms.ModelChoiceField(
        queryset=ProgrammingLanguage.objects.all()
    )

    class Meta:
        model = ProjectProgrammingLanguage
        fields = ("programming_language", "percentage")


ProjectProgrammingLanguageFormSet = inlineformset_factory(
    Project,
    ProjectProgrammingLanguage,
    form=ProgrammingLanguageForm,
    extra=1,
    can_delete=True,
)
