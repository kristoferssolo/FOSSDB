import uuid

from django.conf import settings
from django.db import models

from .host.models import HostingPlatform
from .language.models import ProgrammingLanguage
from .license.models import License
from .operating_system.models import OperatingSystem
from .star.models import Star
from .tag.models import Tag

ser = settings.AUTH_USER_MODEL


class Project(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    licenses = models.ManyToManyField(License)
    programming_languages = models.ManyToManyField(
        ProgrammingLanguage, through="ProjectProgrammingLanguage", related_name="projects")
    hosting_platform = models.ManyToManyField(
        HostingPlatform, through="ProjectHostingPlatform", related_name="projects")
    tag = models.ManyToManyField(Tag)
    os = models.ManyToManyField(OperatingSystem)
    star = models.ManyToManyField(Star, related_name="projects_star")
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def star_amount(self):
        return self.star.count()

    def get_absolute_url(self):
        return f"/{self.author.name}/{self.name}"

    def __str__(self):
        return f"{self.author} | {self.name}"

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid3(
                uuid.uuid4(), f"{self.author.username}-{self.name}")
        super().save(*args, **kwargs)
