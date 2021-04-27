from django.db import models
from .base import Musclegroup


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    primary_musclegroup = models.CharField(max_length=100, choices=Musclegroup.CHOICES)
    secondary_musclegroup = models.CharField(max_length=100, blank=True, null=True, choices=Musclegroup.CHOICES)
    description = models.TextField(max_length=None)

    class Meta:
        ordering = ['name']







