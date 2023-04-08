from django.db import models


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
