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

class FindExerciseByFieldView(APIView):
    def get(self, request, field_value, field_name):
        try:
            # Define a dictionary to map field names to model fields
            field_map = {
                'name': 'name__icontains',
                'primary_muscle': 'primary_muscle__icontains',
                # Add more fields as needed
            }
            
            field_lookup = field_map.get(field_name)
            
            if not field_lookup:
                return Response({'message': 'Invalid field name.'}, status=status.HTTP_400_BAD_REQUEST)
            
            exercises = Exercise.objects.filter(**{field_lookup: field_value})

            if exercises.exists():
                serialized_exercises = ExerciseSerializer(exercises, many=True)
                return Response(serialized_exercises.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': f'No exercises found with that {field_name}.'}, status=status.HTTP_404_NOT_FOUND)
        except Exercise.DoesNotExist:
            return Response({'message': f'No exercises found with that {field_name}.'}, status=status.HTTP_404_NOT_FOUND)