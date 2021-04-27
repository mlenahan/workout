from django.contrib import admin

from .models import Exercise, Set, Workout

admin.site.register(Exercise)
admin.site.register(Set)
admin.site.register(Workout)
