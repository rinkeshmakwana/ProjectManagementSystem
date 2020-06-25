from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return f'{self.user}'
