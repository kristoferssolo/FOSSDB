from django import forms

from .models import License


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ["short_name", "full_name", "url", "description"]
