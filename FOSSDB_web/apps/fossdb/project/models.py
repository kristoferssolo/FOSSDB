import uuid

from django.conf import settings
from django.db import models

from fossdb.hosting_platform.models import (HostingPlatform,
                                            ProjectHostingPlatform)
from fossdb.license.models import License
from fossdb.programming_language.models import (ProgrammingLanguage,
                                                ProjectProgrammingLanguage)
from fossdb.tag.models import Tag

User = settings.AUTH_USER_MODEL


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    licenses = models.ManyToManyField(License)
    programming_languages = models.ManyToManyField(ProgrammingLanguage, through=ProjectProgrammingLanguage, related_name="projects")
    hosting_platform = models.ManyToManyField(HostingPlatform, through=ProjectHostingPlatform, related_name="projects")
    project_type = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid5(uuid.NAMESPACE_URL, f"{self.author.username}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author} | {self.name}"
