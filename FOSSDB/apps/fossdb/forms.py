from django import forms

from .hosting_platform.models import HostingPlatform

from .models import Project


class ProjectForm(forms.ModelForm):
    hosting_platform = forms.ModelChoiceField(queryset=HostingPlatform.objects.all())
    url = forms.URLField(max_length=100)

    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "url",
            "hosting_platform",
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
