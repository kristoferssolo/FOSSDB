import uuid

from django.conf import settings
from django.db import models

from .language.models import ProgrammingLanguage
from .license.models import License

User = settings.AUTH_USER_MODEL


class HostingPlatform(models.Model):
    hosting_platform = models.CharField(max_length=100)

    def __str__(self):
        return self.hosting_platform


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    icon = models.ImageField(upload_to="types/icons/", null=True, blank=True)

    def __str__(self):
        return self.name


class ProjectHostingPlatform(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    hosting_platform = models.ForeignKey(HostingPlatform, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f"{self.project} | {self.hosting_platform}"


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    licenses = models.ManyToManyField(License)
    programming_languages = models.ManyToManyField(ProgrammingLanguage, through="ProjectProgrammingLanguage", related_name="projects")
    hosting_platform = models.ManyToManyField(HostingPlatform, through="ProjectHostingPlatform", related_name="projects")
    tag = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid5(uuid.NAMESPACE_URL, f"{self.author.username}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author} | {self.name}"
