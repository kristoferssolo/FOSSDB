from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default="")



class OperatingSystemVersion(models.Model):
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    version = models.CharField(max_length=50, blank=True, default="")
    codename = models.CharField(max_length=100, blank=True, default="")
    is_lts = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return f"{self.operating_system.name} {self.version} {'LTS' if self.is_lts else ''}"
