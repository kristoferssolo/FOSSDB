from django import forms

from .models import HostingPlatform


class HostingPlatformForm(forms.ModelForm):
    url = forms.URLField()

    class Meta:
        model = HostingPlatform
        fields = ["hosting_platform", "url"]
