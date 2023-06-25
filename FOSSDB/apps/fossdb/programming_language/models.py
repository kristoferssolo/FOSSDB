from django.db import models


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ProjectProgrammingLanguage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.project} | {self.language} | {self.percentage}%"