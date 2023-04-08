from django import forms
from fossdb.models import Project

from .models import HostingPlatform, ProjectHostingPlatform


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
