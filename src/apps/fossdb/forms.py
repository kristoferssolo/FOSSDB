from django import forms

from .models import HostingPlatform, ProgrammingLanguage, Project, ProjectHostingPlatform, ProjectProgrammingLanguage


class HostingPlatformForm(forms.ModelForm):
    class Meta:
        model = ProjectHostingPlatform
        fields = (
            "url",
            "hosting_platform",
        )
        widgets = {
            "hosting_platform": forms.Select(
                choices=HostingPlatform.objects.all(),
            )
        }


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


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "license",
            "tag",
            "operating_system",
        )

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Project name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Description",
                }
            ),
            "license": forms.CheckboxSelectMultiple(),
            "tag": forms.CheckboxSelectMultiple(),
            "operating_system": forms.CheckboxSelectMultiple(),
        }
