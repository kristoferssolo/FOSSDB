from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repo_name

    def get_absolute_url(self):
        return f"/projects/{self.id}"
