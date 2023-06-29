from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "verify form-field submit-form",
            }
        )
        self.fields["username"].label = ""
        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "verify form-field submit-form",
            }
        )
        self.fields["password"].label = ""


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username",
                    "class": "verify form-field submit-form",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email (optional)",
                    "class": "verify form-field submit-form",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={
                    "placeholder": "Password",
                    "class": "verify form-field submit-form",
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "placeholder": "Confirm password",
                    "class": "verify form-field submit-form",
                }
            ),
        }
        labels = {
            "username": "",
            "email": "",
            "password1": "",
            "password2": "",
        }
