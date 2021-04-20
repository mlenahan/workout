from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('exercises/', views.ExerciseList.as_view(), name='exercises'),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercise-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)