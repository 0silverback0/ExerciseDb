# exercises/urls.py
from django.urls import path
from .views import CreateExerciseView, ExerciseDetail, ExerciseList

urlpatterns = [
    path('create/', CreateExerciseView.as_view(), name='create-exercise'),
    path('', ExerciseList.as_view(), name='exercise-list'),
    path('<int:pk>/', ExerciseDetail.as_view(), name='exercise-detail'),
]
