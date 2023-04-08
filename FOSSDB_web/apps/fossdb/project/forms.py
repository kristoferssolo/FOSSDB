from django import forms

from fossdb.hosting_platform.forms import HostingPlatformForm
from fossdb.hosting_platform.models import ProjectHostingPlatform
from fossdb.programming_language.forms import ProgrammingLanguageForm
from fossdb.programming_language.models import ProjectProgrammingLanguage

from .models import Project


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


ProjectHostingPlatformFormSet = forms.inlineformset_factory(
    Project,
    ProjectHostingPlatform,
    form=HostingPlatformForm,
    extra=1,
    can_delete=False
)


ProjectProgrammingLanguageFormSet = forms.inlineformset_factory(
    Project,
    ProjectProgrammingLanguage,
    form=ProgrammingLanguageForm,
    extra=1,
    can_delete=True,
)
