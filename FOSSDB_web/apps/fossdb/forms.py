from django.forms import (CheckboxSelectMultiple, ModelForm,
                          ModelMultipleChoiceField, TextInput)

from .models import License, Project


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ["title", "description", "license"]

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Project name",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Description",
            }),
        }
    license = ModelMultipleChoiceField(queryset=License.objects.all(), widget=CheckboxSelectMultiple)


class LicenseForm(ModelForm):
    class Meta:
        model = License
        fields = ["short_name", "full_name", "url", "description"]
