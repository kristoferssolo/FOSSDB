import uuid

from django.contrib.auth.models import User
from django.db import models

from .license.models import License
from .operating_system.models import OperatingSystemVersion
from .tag.models import Tag


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    license = models.ManyToManyField(License, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    operating_system = models.ManyToManyField(OperatingSystemVersion, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def star_amount(self):
        return self.star.count()

    def get_absolute_url(self):
        return f"/{self.owner}/{self.name}"

    def __str__(self):
        return f"{self.owner} | {self.name}"
