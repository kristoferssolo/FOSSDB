import uuid

from django.contrib.auth.models import User
from django.db import models

from license.models import License


class ProgrammingLanguage(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language


class ProjectProgrammingLanguage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.project} | {self.language} | {self.percentage}%"


class HostingPlatform(models.Model):
    hosting_platform = models.CharField(max_length=100)

    def __str__(self):
        return self.hosting_platform


class ProjectHostingPlatform(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    hosting_platform = models.ForeignKey(HostingPlatform, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f"{self.project} | {self.hosting_platform}"


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    licenses = models.ManyToManyField(License)
    programming_languages = models.ManyToManyField(ProgrammingLanguage, through="ProjectProgrammingLanguage", related_name="projects")
    hosting_platform = models.ManyToManyField(HostingPlatform, through="ProjectHostingPlatform", related_name="projects")
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid5(uuid.NAMESPACE_URL, f"{self.author.username}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author} | {self.name}"
