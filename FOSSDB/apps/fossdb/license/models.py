from django.db import models


class License(models.Model):
    short_name = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100, unique=True)
    url = models.URLField(blank=True, default="")
    text = models.TextField(blank=True, default="")

    def __str__(self):
        return self.short_name
