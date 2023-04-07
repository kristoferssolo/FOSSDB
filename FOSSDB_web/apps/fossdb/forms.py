from django import forms

from .models import License, Project, ProjectProgrammingLanguage


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ["name", "description", "licenses", "programming_languages"]

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
            "programming_languages": forms.CheckboxSelectMultiple(),
        }


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ["short_name", "full_name", "url", "description"]

