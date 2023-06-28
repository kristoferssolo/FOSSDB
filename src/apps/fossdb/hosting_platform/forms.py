from django import forms

from .models import HostingPlatform, ProjectHostingPlatform


class HostingPlatformForm(forms.ModelForm):
    class Meta:
        model = ProjectHostingPlatform
        fields = (
            "url",
            "hosting_platform",
        )
        widgets = {
            "hosting_platform": forms.Select(
                choices=HostingPlatform.objects.all(),
            )
        }
