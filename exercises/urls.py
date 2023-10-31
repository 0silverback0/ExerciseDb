# exercises/urls.py
from django.urls import path
from .views import CreateExerciseView, ExerciseDetail, ExerciseList, FindExerciseByNameView, FindExerciseByPrimaryMuscleView

urlpatterns = [
    path('create/', CreateExerciseView.as_view(), name='create-exercise'),
    path('', ExerciseList.as_view(), name='exercise-list'),
    path('<int:pk>/', ExerciseDetail.as_view(), name='exercise-detail'),
    path('name/<str:name>', FindExerciseByNameView.as_view(), name='search'),
    path('primary-muscle/<str:primary_muscle>', FindExerciseByPrimaryMuscleView.as_view(), name='primary-muscle')
]
