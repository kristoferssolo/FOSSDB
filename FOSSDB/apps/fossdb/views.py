from django import forms
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .forms import ProjectForm
from .hosting_platform.forms import HostingPlatformForm
from .models import Project
from .programming_language.forms import ProgrammingLanguageForm


@login_required(login_url="login/")
@permission_required("fossdb.add_project", login_url="login/", raise_exception=True)
def add_project(request):
    project_form = ProjectForm(request.POST or None)
    hosting_platform_form = HostingPlatformForm(request.POST or None)
    programming_language_form = ProgrammingLanguageForm(request.POST or None)

    _forms: dict[str, forms.ModelForm] = {
        "project_form": project_form,
        "hosting_platform_form": hosting_platform_form,
        "programming_language_form": programming_language_form,
    }

    if request.method == "POST":
        if all([form.is_valid() for form in _forms.values()]):
            project = project_form.save(commit=False)
            project.author = request.user
            project.save()

            hosting_platform = hosting_platform_form.save(commit=False)
            hosting_platform.project = project
            hosting_platform.save()

            # TODO: allow adding multiple languages
            programming_language = programming_language_form.save(commit=False)
            programming_language.project = project
            programming_language.save()

            project.save_m2m()
            return redirect("index")

    context = {"title": "Add project", **_forms}
    return render(request, "fossdb/add_project.html", context)


def index(request):
    context = {
        "title": "FOSSDB",
        "projects": Project.objects.all(),
    }
    return render(request, "fossdb/index.html", context)







