from django.db import models
from django.contrib.auth.models import User

status = (
    ('1', 'New'),
    ('2', 'In Progress'),
    ('3', 'Completed'),
    ('4', 'Cancelled'),
)


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    status = models.CharField(max_length=4, choices=status, default=1)
    assign = models.ManyToManyField(User)

    class Meta:
        ordering = ['project_name']

    def __str__(self):
        return self.project_name
