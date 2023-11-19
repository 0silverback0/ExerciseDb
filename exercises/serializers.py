# exercises/serializers.py
from rest_framework import serializers
from .models import Exercise

PRIMARY_MUSCLE_CHOICES = [
    ('chest', 'Chest'),
    ('back', 'Back'),
    ('quadriceps', 'Quads'),
    ('shoulders', 'Shoulders'),
    ('arms', 'Arms'),
    ('abs', 'Abs'),
]

class ExerciseSerializer(serializers.ModelSerializer):
    primary_muscle = serializers.ChoiceField(choices=PRIMARY_MUSCLE_CHOICES)

    class Meta:
        model = Exercise
        fields = '__all__'