from django.db import models


class HostingPlatform(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ProjectHostingPlatform(models.Model):
    hosting_platform = models.ForeignKey(HostingPlatform, on_delete=models.CASCADE)
    project = models.OneToOneField("Project", on_delete=models.CASCADE)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url
