from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .forms import ProjectForm
from .hosting_platform.forms import ProjectHostingPlatformForm
from .hosting_platform.models import ProjectHostingPlatform
from .models import Project


@login_required(login_url="login/")
@permission_required("fossdb.add_project", login_url="login/", raise_exception=True)
def add_project(request):
    project_form = ProjectForm(request.POST or None)
    hosting_platform_form = ProjectHostingPlatformForm(request.POST or None)

    if request.method == "POST":
        if project_form.is_valid() and hosting_platform_form.is_valid():
            project = project_form.save(commit=False)
            project.author = request.user
            project.save()

            project_hosting_platform = ProjectHostingPlatform(
                hosting_platform=hosting_platform_form.cleaned_data["hosting_platform"],
                project=project,
                url=hosting_platform_form.cleaned_data["url"],
            )
            project_hosting_platform.save()

            project_form.save_m2m()
            return redirect("index")

    context = {
        "title": "Add project",
        "form": project_form,
        "host_form": hosting_platform_form,
    }
    return render(request, "fossdb/add_project.html", context)


def index(request):
    context = {
        "title": "FOSSDB",
        "projects": Project.objects.all(),
    }
    return render(request, "fossdb/index.html", context)







