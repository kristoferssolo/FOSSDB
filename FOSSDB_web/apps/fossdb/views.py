from django.contrib.auth.decorators import login_required, permission_required
from django.forms import formset_factory
from django.shortcuts import redirect, render

from .forms import ProjectForm, ProjectProgrammingLanguageForm
from .models import ProgrammingLanguage, Project


def index(request):
    context = {
        "title": "FOSSDB",
        "projects": Project.objects.all(),
    }
    return render(request, "fossdb/index.html", context)


@login_required(login_url="login/")
@permission_required("fossdb.add_post", login_url="login/", raise_exception=True)
def add_project(request):
    ProgrammingLanguageFormSet = formset_factory(ProjectProgrammingLanguageForm, extra=1)
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        language_formset = ProgrammingLanguageFormSet(request.POST)

        if project_form.is_valid() and language_formset.is_valid():
            project = project_form.save(commit=False)
            project.author = request.user
            project.save()

            for language_form in language_formset:
                if language_formset.is_valid():
                    language = language_form.save(commit=False)
                    language.project = project
                    language.save()

            project_form.save_m2m()
            return redirect("/")
    else:
        project_form = ProjectForm()
        language_formset = ProgrammingLanguageFormSet()

    context = {
        "title": "Add project",
        "project_form": project_form,
        "language_formset": language_formset
    }
    return render(request, "fossdb/add_project.html", context)
