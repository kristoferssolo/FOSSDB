from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

from .forms import ProjectForm
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, "fossdb/index.html", {"title": "FOSSDB", "projects": projects})


@login_required(login_url="login/")
@permission_required("fossdb.add_post)", login_url="login/", raise_exception=True)
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/")
    else:
        form = ProjectForm()
    return render(request, "fossdb/add_project.html", {"title": "Add project", "form": form})
