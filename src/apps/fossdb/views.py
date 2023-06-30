from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import HostingPlatformForm, ProgrammingLanguageInlineFormSet, ProjectForm
from .models import Project


class SearchResultsListView(ListView):
    model = Project
    template_name = "search.html"
    context_object_name = "projects"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Project.objects.filter(
            Q(owner__username__icontains=query)
            | Q(name__icontains=query)
            # | Q(description__icontains=query)
            | Q(license__short_name__icontains=query)
            | Q(license__full_name__icontains=query)
            | Q(tag__name__icontains=query)
            | Q(operating_system__operating_system__name__icontains=query)
            | Q(operating_system__codename__icontains=query)
            | Q(programming_language__name__icontains=query)
        ).distinct()

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "FOSSDB | Search"
        return data


class ProfileProjectListView(ListView):
    model = Project
    template_name = "profile.html"
    context_object_name = "projects"
    slug_field = "username"

    def get_queryset(self):
        username = self.kwargs.get("username")
        self.user = get_object_or_404(get_user_model(), username=username)
        return Project.objects.filter(owner__username=username).order_by("-date_created")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = self.user.username + ("" if not self.user.full_name else f" ({self.user.full_name})")
        data["page_owner"] = self.user
        return data


class ProjectListView(ListView):
    model = Project
    template_name = "explore.html"
    context_object_name = "projects"
    paginate_by = 50  # amount of items on screen

    def get_queryset(self):
        return Project.objects.order_by("-date_created")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "FOSSDB | Explore"
        return data


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "create_view.html"
    login_url = reverse_lazy("login")
    redirect_field_name = "redirect_to"

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "FOSSDB | Create Project"
        data["hosting_platform"] = HostingPlatformForm(self.request.POST or None)
        data["programming_languages"] = ProgrammingLanguageInlineFormSet(self.request.POST or None)
        return data

    def form_valid(self, form):
        context = self.get_context_data()

        form.instance.owner = self.request.user

        self.object = form.save()  # Save project form

        hosting_platform = context["hosting_platform"]
        if hosting_platform.is_valid():
            hosting_platform = hosting_platform.save(commit=False)
            hosting_platform.project = self.object
            hosting_platform.save()

        programming_languages = context["programming_languages"]
        if programming_languages.is_valid():
            programming_languages.instance = self.object
            programming_languages.save()

        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project
    template_name = "detailed_view.html"
    context_object_name = "project"
    slug_field = "name"
    slug_url_kwarg = "project_name"


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = "create_view.html"
    form_class = ProjectForm
    slug_field = "name"
    slug_url_kwarg = "project_name"
    login_url = reverse_lazy("login")
    redirect_field_name = "redirect_to"

    def test_func(self):
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        return redirect("login")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = f"Edit {self.object}"
        data["hosting_platform"] = HostingPlatformForm(self.request.POST or None, instance=self.object.projecthostingplatform)
        data["programming_languages"] = ProgrammingLanguageInlineFormSet(self.request.POST or None, instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()

        form.instance.owner = self.request.user

        self.object = form.save()  # Save project form

        hosting_platform = context["hosting_platform"]
        if hosting_platform.is_valid():
            hosting_platform.project = self.object
            hosting_platform.save()

        programming_languages = context["programming_languages"]
        if programming_languages.is_valid():
            programming_languages.instance = self.object
            programming_languages.save()

        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "delete_view.html"
    slug_field = "name"
    slug_url_kwarg = "project_name"
    login_url = reverse_lazy("login")
    redirect_field_name = "redirect_to"
    success_url = reverse_lazy("explore")

    def test_func(self):
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        return redirect("login")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = f"Delete {self.object}"
        return data
