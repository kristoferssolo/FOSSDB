from django import forms

from .models import HostingPlatform, ProjectHostingPlatform


class ProjectHostingPlatformForm(forms.ModelForm):
    hosting_platform = forms.ModelChoiceField(queryset=HostingPlatform.objects.all())

    class Meta:
        model = ProjectHostingPlatform
        fields = ("hosting_platform", "url")
