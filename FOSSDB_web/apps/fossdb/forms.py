from django import forms

from .models import HostingPlatform, License, Project, ProjectHostingPlatform


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


class HostingPlatformForm(forms.ModelForm):
    url = forms.URLField()

    class Meta:
        model = HostingPlatform
        fields = ["hosting_platform", "url"]


ProjectHostingPlatformFormSet = forms.inlineformset_factory(
    Project,
    ProjectHostingPlatform,
    form=HostingPlatformForm,
    extra=1,
    can_delete=False
)
