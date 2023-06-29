from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from fossdb.models import Project

from .forms import LoginForm, SignUpForm
from .models import User


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


def profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        "title": user.username + ("" if not user.full_name else f" ({user.full_name})"),
        "user": user,
    }
    return render(request, "profile.html", context)


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
