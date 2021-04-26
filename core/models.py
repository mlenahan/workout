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

    def __str__(self):
        return self.name


class Set(models.Model):
    exercise = models.ForeignKey('core.Exercise', null=False, blank=False, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField(null=False, blank=False, default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(null=False, blank=True, max_length=1000)
    number_of_sets = models.IntegerField(null=False, blank=False, default=3)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.exercise) + ' - ' + str(self.reps) + ' - ' + str(self.weight)


class Workout(models.Model):
    name = models.CharField(max_length=255, null=True)
    exercise = models.ManyToManyField('core.Exercise')
    set = models.ManyToManyField('core.Set')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)



# Workout -> User, CreatedAt, FinishedAt,

# Set -> Workout(many to one), Reps, Exercise(many to one), Weight, Notes,  CreatedAt, RestTime??

# ExerciseTag -> e.g. Quads, hamstrings..., Name, (many to many(put on exercise model))

# User ->

# TODO - model all of the above