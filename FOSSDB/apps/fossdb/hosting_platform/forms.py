from django import forms

from .models import ProjectHostingPlatform, HostingPlatform


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
