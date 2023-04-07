from django import forms

from .models import (License, ProgrammingLanguage, Project,
                     ProjectProgrammingLanguage)


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ["name", "description", "licenses"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Project name",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description",
            }),
            "licenses": forms.CheckboxSelectMultiple(),
        }


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ["short_name", "full_name", "url", "description"]

