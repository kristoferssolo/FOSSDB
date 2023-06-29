import uuid
from pathlib import Path

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def get_profile_pic_path(instance, filename) -> Path:
    ext = filename.split(".")[-1]
    filename = f"{instance.id}.{ext}"
    return Path("profile_pics", filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")

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

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=get_profile_pic_path, default="profile-pics/default.jpg")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwags):
        old_instance = None
        if self.pk:
            try:
                old_instance = User.objects.get(pk=self.pk)
            except ObjectDoesNotExist:
                pass
        super(Profile, self).save(*args, **kwags)

        # Check if old instance exists and profile picture is different
        if old_instance is not None:
            if old_instance.profile_picture and self.picture and old_instance.profile_picture.url != self.picture.url:
                old_instance.profile_picture.delete(save=False)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwags):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwags):
    instance.profile.save()
