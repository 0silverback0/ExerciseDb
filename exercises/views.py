from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Exercise
from .serializers import ExerciseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateExerciseView(generics.CreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseList(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class FindExerciseByNameView(APIView):
    def get(self, request, name):
        try:
            exercises = Exercise.objects.filter(name__icontains=name)
            
            if exercises.exists():
                serialized_exercises = ExerciseSerializer(exercises, many=True)
                return Response(serialized_exercises.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No exercises found with that name.'}, status=status.HTTP_404_NOT_FOUND)
        except Exercise.DoesNotExist:
            return Response({'message': 'No exercises found with that name.'}, status=status.HTTP_404_NOT_FOUND)
        
class FindExerciseByPrimaryMuscleView(APIView):
    def get(self, request, primary_muscle):
        try:
            exercises = Exercise.objects.filter(primary_muscle__icontains=primary_muscle)

            if exercises.exists():
                serialized_exercises = ExerciseSerializer(exercises, many=True)
                return Response(serialized_exercises.data, status=status.HTTP_200_OK)
            else:
                  return Response({'message': 'No exercises found with that primary muscle.'}, status=status.HTTP_404_NOT_FOUND)
        except Exercise.DoesNotExist:
            return Response({'message': 'No exercises found with that primary muscle.'}, status=status.HTTP_404_NOT_FOUND)
        