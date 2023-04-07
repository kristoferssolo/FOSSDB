from django.contrib.auth.models import User
from django.db import models


class License(models.Model):
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.short_name


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    license = models.ManyToManyField(License)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repo_name

    def get_absolute_url(self):
        return f"/projects/{self.id}"
