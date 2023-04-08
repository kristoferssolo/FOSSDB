from django import forms

from .models import ProgrammingLanguage


class ProgrammingLanguageForm(forms.ModelForm):
    percentage = forms.IntegerField(min_value=0, max_value=100)

    class Meta:
        model = ProgrammingLanguage
        fields = ["language", "percentage"]
