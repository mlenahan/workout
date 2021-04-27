from django.db import models


class Exercise(models.Model):
    name = models.CharField(
        max_length=255,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.TextField(
        max_length=None,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(
        max_length=255,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class Set(models.Model):
    exercise = models.ForeignKey(
        'core.Exercise',
        on_delete=models.CASCADE
    )
    workout = models.ForeignKey(
        'core.Workout',
        on_delete=models.CASCADE
    )
    reps = models.PositiveIntegerField(
        default=0,
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    # weight measurement?
    notes = models.TextField(
        null=True,
        blank=True,
        max_length=1000,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return str(self.exercise) + ' - ' + str(self.reps) + ' - ' + str(self.weight)
