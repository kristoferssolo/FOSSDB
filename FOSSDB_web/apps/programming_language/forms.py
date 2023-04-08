from django import forms
from fossdb.models import Project

from .models import ProgrammingLanguage, ProjectProgrammingLanguage


class ProgrammingLanguageForm(forms.ModelForm):
    percentage = forms.IntegerField(min_value=0, max_value=100)

    class Meta:
        model = ProgrammingLanguage
        fields = ["language", "percentage"]


ProjectProgrammingLanguageFormSet = forms.inlineformset_factory(
    Project,
    ProjectProgrammingLanguage,
    form=ProgrammingLanguageForm,
    extra=1,
    can_delete=True,
)
