from django import forms
from django.forms import inlineformset_factory

from .models import HostingPlatform, License, OperatingSystemVersion, ProgrammingLanguage, Project, ProjectHostingPlatform, ProjectProgrammingLanguage, Tag


class HostingPlatformForm(forms.ModelForm):
    class Meta:
        model = ProjectHostingPlatform
        fields = (
            "hosting_platform",
            "url",
        )
        widgets = {
            "hosting_platform": forms.Select(
                choices=HostingPlatform.objects.all(),
                attrs={
                    "class": "form-field submit-form",
                },
            ),
            "url": forms.URLInput(
                attrs={
                    "placeholder": "url",
                    "class": "form-field submit-form font-roboto",
                },
            ),
        }
        labels = {
            "hosting_platform": "",
            "url": "",
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
                attrs={
                    "class": "form-field submit-form",
                },
            ),
            "percentage": forms.NumberInput(
                attrs={
                    "placeholder": "Percentage",
                    "class": "form-field submit-form",
                    "min": "0",
                    "max": "100",
                },
            ),
        }
        labels = {
            "programming_language": "",
            "percentage": "",
        }


ProgrammingLanguageInlineFormSet = inlineformset_factory(
    Project,
    ProjectProgrammingLanguage,
    form=ProgrammingLanguageForm,
    extra=0,
    can_delete=True,
)


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
                    "placeholder": "Project name",
                    "class": "form-field submit-form font-roboto",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Description",
                    "class": "form-field submit-form font-roboto",
                },
            ),
            "license": forms.CheckboxSelectMultiple(
                choices=License.objects.all(),
                attrs={
                    "class": "checkbox-form",
                },
            ),
            "operating_system": forms.CheckboxSelectMultiple(
                choices=OperatingSystemVersion.objects.all(),
                attrs={
                    "class": "checkbox-form",
                },
            ),
            "tag": forms.CheckboxSelectMultiple(
                choices=Tag.objects.all(),
                attrs={
                    "class": "checkbox-form",
                },
            ),
        }
        labels = {
            "name": "",
            "description": "",
            "license": "",
            "tag": "",
            "operating_system": "",
        }
