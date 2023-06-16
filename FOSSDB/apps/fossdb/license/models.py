from django.db import models


class License(models.Model):
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, blank=True, default="")
    url = models.URLField(blank=True, default="")
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.short_name
