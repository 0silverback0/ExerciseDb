# exercises/urls.py
from django.urls import path
from .views import CreateExerciseView, ExerciseDetail, ExerciseList, FindExerciseByFieldView

urlpatterns = [
    path('create/', CreateExerciseView.as_view(), name='create-exercise'),
    path('', ExerciseList.as_view(), name='exercise-list'),
    path('<int:pk>/', ExerciseDetail.as_view(), name='exercise-detail'),
    path('<str:field_name>/<str:field_value>', FindExerciseByFieldView.as_view(), name='search'),
    path('<str:field_name>/<str:field_value>', FindExerciseByFieldView.as_view(), name='primary-muscle')
]
