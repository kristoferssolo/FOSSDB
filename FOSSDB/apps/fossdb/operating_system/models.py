from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")
    version = models.CharField(max_length=50, blank=True)
