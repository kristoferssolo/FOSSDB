from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

from .forms import (ProjectForm, ProjectHostingPlatformFormSet,
                    ProjectProgrammingLanguageFormSet)
from .models import Project


def index(request):
    context = {
        "title": "FOSSDB",
        "projects": Project.objects.all(),
    }
    return render(request, "fossdb/index.html", context)


@login_required(login_url="login/")
@permission_required("fossdb.add_project", login_url="login/", raise_exception=True)
def add_project(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        language_formset = ProjectProgrammingLanguageFormSet(request.POST, instance=Project())
        host_formset = ProjectHostingPlatformFormSet(request.POST, instance=Project())

        if project_form.is_valid() and language_formset.is_valid() and host_formset.is_valid():
            project = project_form.save(commit=False)
            project.author = request.user
            project.save()

            language_formset.instance = project
            language_formset.save()

            host_formset.instance = project
            host_formset.save()

            project_form.save_m2m()
            return redirect("/")
    else:
        project_form = ProjectForm()
        language_formset = ProjectProgrammingLanguageFormSet()
        host_formset = ProjectHostingPlatformFormSet()

    context = {
        "title": "Add project",
        "project_form": project_form,
        "language_formset": language_formset,
        "host_formset": host_formset,
    }
    return render(request, "fossdb/add_project.html", context)
