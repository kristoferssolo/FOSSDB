from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to="types/icons/", null=True, blank=True)
