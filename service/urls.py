from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('exercises/', views.ExerciseList.as_view()),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)