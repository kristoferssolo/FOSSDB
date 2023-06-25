from django import forms

from .hosting_platform.models import HostingPlatform

from .models import Project


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

        exclude = ("programming_language",)

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
