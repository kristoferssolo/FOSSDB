import uuid

from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    licenses = models.ManyToManyField("License")
    programming_languages = models.ManyToManyField("ProgrammingLanguage", through="ProjectProgrammingLanguage", related_name="projects")
    hosting_platform = models.ManyToManyField("HostingPlatform", through="ProjectHostingPlatform", related_name="projects")
    tag = models.ManyToManyField("Tag")
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid5(uuid.NAMESPACE_URL, f"{self.author.username}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author} | {self.name}"
