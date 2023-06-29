from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from django_filters.views import FilterView

from .filters import ProjectFilter

from .forms import HostingPlatformForm, ProgrammingLanguageInlineFormSet, ProjectForm
from .models import Project


class ProjectListView(FilterView):
    model = Project
    template_name = "explore.html"
    filterset_class = ProjectFilter
    context_object_name = "projects"
    paginate_by = 100  # optional 10 projects a page


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "create_view.html"
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
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
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def test_func(self):
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        return redirect("login")

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)
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
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    success_url = "/"

    def test_func(self):
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        return redirect("login")
