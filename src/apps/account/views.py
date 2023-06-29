from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView, View

from fossdb.models import Project

from .forms import LoginForm, SignUpForm, UserChangeForm


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = "setting.html"
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def get(self, request):
        user_form = UserChangeForm(instance=request.user)
        context = {
            "title": "Your profile",
            "user_form": user_form,
        }
        return self.render_to_response(context)

    def post(self, request):
        user_form = UserChangeForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.add_message(request, messages.SUCCESS, "Your profile was successfully updated!")

        context = {
            "title": "Your profile",
            "user_form": user_form,
        }
        return self.render_to_response(context)


class PasswordChangeView(LoginRequiredMixin, TemplateView):
    template_name = "password.html"

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        context = {
            "title": "Change password",
            "form": form,
        }
        return self.render_to_response(context)

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()

            update_session_auth_hash(request, form.user)
            messages.add_message(request, messages.SUCCESS, "Your password was successfully updated!")

        context = {
            "title": "Change password",
            "form": form,
        }
        return self.render_to_response(context)


class ProfileProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "profile.html"
    context_object_name = "projects"
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = self.request.user.username + ("" if not self.request.user.full_name else f" ({self.request.user.full_name})")
        return data


def signup_view(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("homepage")

    context = {
        "title": "FOSSDB | SignUp",
        "form": form,
    }
    return render(request, "signup.html", context)


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("homepage")

    context = {
        "title": "FOSSDB | Login",
        "form": form,
    }
    return render(request, "login.html", context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
