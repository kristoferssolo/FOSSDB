from django import forms

from .models import (HostingPlatform, License, ProgrammingLanguage, Project,
                     ProjectHostingPlatform, ProjectProgrammingLanguage)


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
