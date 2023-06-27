import uuid
from pathlib import Path

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


def get_profile_pic_path(instance, filename) -> Path:
    ext = filename.split(".")[-1]
    filename = f"{instance.id}.{ext}"
    return Path("profile_pics", filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    profile_picture = models.ImageField(upload_to=get_profile_pic_path, default=Path("profile_pic", "default.jpg"))

    @property
    def full_name(self):
        if not self.first_name and not self.last_name:
            return ""
        elif self.first_name and not self.last_name:
            return self.first_name
        elif not self.first_name and self.last_name:
            return self.last_name
        else:
            return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwags):
        old_instance = None
        if self.pk:
            try:
                old_instance = User.objects.get(pk=self.pk)
            except ObjectDoesNotExist:
                pass
        super(User, self).save(*args, **kwags)

        # Check if old instance exists and profile picture is different
        if old_instance is not None:
            if old_instance.profile_picture and self.profile_picture and old_instance.profile_picture.url != self.profile_picture.url:
                old_instance.profile_picture.delete(save=False)
