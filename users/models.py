from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

employee_type = (
    ('1', 'Developer'),
    ('2', 'Team Lead'),
    ('3', 'Project Manager'),
)

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emp_type = models.CharField(max_length=3, choices=employee_type, default=1)
    project = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return f'{self.user}'
