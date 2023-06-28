import uuid

from django.conf import settings

from django.db import models


class License(models.Model):
    short_name = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100, unique=True)
    url = models.URLField(blank=True, default="")
    text = models.TextField(blank=True, default="")

    def __str__(self):
        return self.short_name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name


class OperatingSystemVersion(models.Model):
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    version = models.CharField(max_length=50, blank=True, default="")
    codename = models.CharField(max_length=100, blank=True, default="")
    is_lts = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return f"{self.operating_system.name} {self.version} {'LTS' if self.is_lts else ''}"

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "operating_system",
                    "version",
                ),
                name="unique_os_version",
            ),
        )


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True, default="")
    icon = models.ImageField(upload_to="tags/icons/", null=True, blank=True)

    def __str__(self):
        return self.name


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    license = models.ManyToManyField(License, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    operating_system = models.ManyToManyField(OperatingSystemVersion, blank=True)
    programming_language = models.ManyToManyField(ProgrammingLanguage, through="ProjectProgrammingLanguage", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def star_amount(self):
        return self.star.count()

    def get_absolute_url(self):
        return f"/{self.owner}/{self.name}"

    def __str__(self):
        return f"{self.owner}/{self.name}"

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "owner",
                    "name",
                ),
                name="unique_owner_name",
            ),
        )


class ProjectProgrammingLanguage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    programming_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
    percentage = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.project.owner}/{self.project.name} | {self.programming_language} | {self.percentage}%"


class HostingPlatform(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ProjectHostingPlatform(models.Model):
    hosting_platform = models.ForeignKey(HostingPlatform, on_delete=models.CASCADE)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url


class Star(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
