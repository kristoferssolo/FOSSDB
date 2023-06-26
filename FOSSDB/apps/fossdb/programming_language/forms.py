from django import forms

from .models import ProgrammingLanguage, ProjectProgrammingLanguage


class ProgrammingLanguageForm(forms.ModelForm):
    class Meta:
        model = ProjectProgrammingLanguage
        fields = (
            "programming_language",
            "percentage",
        )
        widgets = {
            "programming_language": forms.Select(
                choices=ProgrammingLanguage.objects.all(),
            ),
            "percentage": forms.NumberInput(
                attrs={
                    "min": "0",
                    "max": "100",
                }
            ),
        }
