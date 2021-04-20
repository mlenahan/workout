import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from core.models import Exercise
from service.serializers import ExerciseSerializer

client = Client()


class GetAllExercisesTest(TestCase):

    def setUp(self):
        Exercise.objects.create(
            name='Deadlift', primary_musclegroup='Back', secondary_musclegroup='Quads',
            description='random description')
        Exercise.objects.create(
            name='Back Squat', primary_musclegroup='Quads', secondary_musclegroup='Hamstrings',
            description='random description blah blah')
        Exercise.objects.create(
            name='Skull Crusher', primary_musclegroup='Triceps', secondary_musclegroup='',
            description='random description blah blah blah')

    def test_get_all_exercises(self):
        response = client.get(reverse('exercises'))

        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewExerciseTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'name': 'Hammer Curl',
            'primary_musclegroup': 'Biceps',
            'secondary_musclegroup': '',
            'description': 'Fake Description about hammer curl'
        }
        self.invalid_payload = {
            'name': '',
            'primary_musclegroup': 'Biceps',
            'secondary_musclegroup': 'Triceps',
            'description': 'Fake description about fake exercise'
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('exercises'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('exercises'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetExerciseDetailTest(TestCase):

    def setUp(self):
        self.exercise = Exercise.objects.create(name='Test Exercise')

    def test_successful_response(self):
        url = reverse('exercise-detail', kwargs={'pk': self.exercise.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_bad_id(self):
        url = reverse('exercise-detail', kwargs={'pk': self.exercise.pk + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class UpdateSingleExerciseTest(TestCase):

    def setUp(self):
        self.squat = Exercise.objects.create(
            name='Squat', primary_musclegroup='Quads', secondary_musclegroup='Hamstrings',
            description='Random description about squat')
        self.benchpress = Exercise.objects.create(
            name='Benchpress', primary_musclegroup='Chest', secondary_musclegroup='Triceps',
            description='Random Description about benchpress')
        self.valid_payload = {
            'name': 'Benchpress',
            'primary_musclegroup': 'Chest',
            'secondary_musclegroup': 'Hamstrings',
            'description': 'Random Description about benchpress'
        }
        self.invalid_payload = {
            'name': '',
            'primary_musclegroup': 'Back',
            'secondary_musclegroup': 'Triceps',
            'description': 'Random fake description'
        }

    def test_valid_update_exercise(self):
        response = client.put(
            reverse('exercise-detail', kwargs={'pk': self.benchpress.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_puppy(self):
        response = client.put(
            reverse('exercise-detail', kwargs={'pk': self.benchpress.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleExerciseTest(TestCase):

    def setUp(self):
        self.squat = Exercise.objects.create(
            name='Squat', primary_musclegroup='Quads', secondary_musclegroup='Hamstrings',
            description='Random description about squat')
        self.benchpress = Exercise.objects.create(
            name='Benchpress', primary_musclegroup='Chest', secondary_musclegroup='Triceps',
            description='Random Description about benchpress')

    def test_valid_delete_exercise(self):
        response = client.delete(
            reverse('exercise-detail', kwargs={'pk': self.squat.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_exercise(self):
        response = client.delete(
            reverse('exercise-detail', kwargs={'pk': 30000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)