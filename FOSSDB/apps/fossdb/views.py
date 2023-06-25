from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .forms import ProjectForm
from .hosting_platform.models import ProjectHostingPlatform
from .models import Project


@login_required(login_url="login/")
@permission_required("fossdb.add_project", login_url="login/", raise_exception=True)
def add_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project_hosting_platform = ProjectHostingPlatform.objects.create(
                hosting_platform=form.cleaned_data["hosting_platform"],
                url=form.cleaned_data["url"],
            )
            project.hosting_platform = project_hosting_platform
            project.save()

            form.save_m2m()
            return redirect("index")

    context = {
        "title": "Add project",
        "form": form,
    }
    return render(request, "fossdb/add_project.html", context)


def index(request):
    context = {
        "title": "FOSSDB",
        "projects": Project.objects.all(),
    }
    return render(request, "fossdb/index.html", context)







