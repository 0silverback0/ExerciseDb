import os
from django.core.management.base import BaseCommand
import json
from exercises.models import Exercise  # Adjust based on your app and model names

class Command(BaseCommand):
    help = 'Seed exercise data from JSON file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join('exercises', 'management', 'commands', 'exercise_seed_data.json')

        with open(file_path, 'r') as file:
            exercise_data = json.load(file)

        for data in exercise_data:
            Exercise.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Exercise data successfully seeded'))
