import json

from rest_framework.test import APITestCase

from users.models import User
from .models import Lesson


class LessonsTestCase(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='yusif.alik@mail.rufduu')
        self.user.set_password('12333')
        self.user.save()
        response = self.client.post('/api/token/',
                                    {"email": "yusif.alik@mail.rufduu", "password": "12333"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'JWToken {self.access_token}')

    def test_getting_lessons_list(self):
        response = self.client.get(
            '/api/v1/lessons/list/'
        )

        self.assertEqual(
            response.json(),
            []
        )
