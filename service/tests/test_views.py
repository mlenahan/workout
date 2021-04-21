import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from core.models import Exercise
from core.base import Musclegroup
from service.serializers import ExerciseSerializer

client = Client()

CONTENT_TYPE = 'application/json'


class TestMixin:
    def create_test_exercise(self, **kwargs):
        kwargs.setdefault('name', 'Bench Press')
        kwargs.setdefault('primary_musclegroup', Musclegroup.CHEST)
        kwargs.setdefault('secondary_musclegroup', Musclegroup.TRICEPS)
        kwargs.setdefault('description', ' Random description about bench press')
        return Exercise.objects.create(**kwargs)

    def get_url(self, **kwargs):
        return reverse(self.url_name, kwargs=kwargs)


class GetAllExercisesTest(TestCase, TestMixin):

    url_name = 'exercises'

    def setUp(self):
        self.create_test_exercise()
        self.create_test_exercise()
        self.create_test_exercise()

    def test_get_all_exercises(self):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        response = client.get(self.get_url())
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewExerciseTest(TestCase, TestMixin):

    url_name = 'exercises'

    def setUp(self):
        self.payload = {
            'name': 'Hammer Curl',
            'primary_musclegroup': 'Biceps',
            'secondary_musclegroup': '',
            'description': 'Fake Description about hammer curl'
        }

    def make_request(self):
        return client.post(
            self.get_url(),
            data=json.dumps(self.payload),
            content_type=CONTENT_TYPE
        )

    def test_create_valid(self):
        response = self.make_request()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self):
        self.payload['name'] = ''
        response = self.make_request()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetExerciseDetailTest(TestCase, TestMixin):

    url_name = 'exercise-detail'

    def setUp(self):
        self.exercise = self.create_test_exercise()

    def test_successful_response(self):
        serializer = ExerciseSerializer(self.exercise)
        url = self.get_url(pk=self.exercise.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_bad_id(self):
        url = self.get_url(pk=self.exercise.pk + 1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class UpdateSingleExerciseTest(TestCase, TestMixin):

    url_name = 'exercise-detail'

    def setUp(self):
        self.exercise = self.create_test_exercise()
        self.payload = {
            'name': 'Benchpress',
            'primary_musclegroup': 'Chest',
            'secondary_musclegroup': 'Hamstrings',
            'description': 'Random Description about benchpress'
        }

    def test_valid_update(self):
        response = client.put(
            self.get_url(pk=self.exercise.pk),
            data=json.dumps(self.payload),
            content_type=CONTENT_TYPE
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update(self):
        self.payload['name'] = ''
        response = client.put(
            self.get_url(pk=self.exercise.pk),
            data=json.dumps(self.payload),
            content_type=CONTENT_TYPE)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleExerciseTest(TestCase, TestMixin):

    url_name = 'exercise-detail'

    def setUp(self):
        self.exercise = self.create_test_exercise()

    def test_valid_delete(self):
        response = client.delete(self.get_url(pk=self.exercise.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = client.delete(self.get_url(pk=self.exercise.pk + 1))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
