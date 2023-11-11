from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Exercise
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TestExerciseViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def create_test_data(self, name):
        return {
            'name': name,
            'primary_muscle': 'chest',
            'exercise_type': 'push',
            'other_names': 'test',
            'image_url': 'https://example.com/exercise_image.jpg',
            'video_url': 'https://example.com/exercise_video.mp4',
            'instructions': 'coming soon',
            'equipment': 'barbell'
        }

    def test_create_exercise_view(self):
        exercise_data = self.create_test_data('Unique Name 1')
        response = self.client.post('/api/exercises/create/', exercise_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_exercises_view(self):
        response = self.client.get('/api/exercises/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_exercise(self):
        exercise_data = self.create_test_data('Unique Name 2')
        created_exercise = Exercise.objects.create(**exercise_data)
        response = self.client.get(f'/api/exercises/{created_exercise.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)