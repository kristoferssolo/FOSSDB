from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Star(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="stars")
