from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase

from user_profile.models import UserProfile


class UserProfileListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='cosmef',
            first_name='cosme',
            last_name='fulanito',
            email='cosme@localhost',
        )
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_user_profile_list(self):
        url = reverse('user_profile_list')
        response = self.client.get(url)
        data = response.data
        data = data[0]
        data = data.get('user')
        self.assertEqual('cosmef', data.get('username'))
        self.assertEqual('cosme', data.get('first_name'))
        self.assertEqual('fulanito', data.get('last_name'))
        self.assertEqual('cosme@localhost', data.get('email'))
        self.assertEqual(200, response.status_code)


class UserProfileCreateAPIViewTestCase(APITestCase):
    def SetUp(self):
        pass

    def test_user_profile_create_succes(self):
        url = reverse('user_profile_create')
        data = {
            "user": {
                "username": "cosmef",
                "first_name": "Cosme",
                "last_name": "Fulanito",
                "email": "cosme@localhost"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(200, response.status_code)

    def test_user_profile_create_fail(self):
        url = reverse('user_profile_create')
        data = {"user": {}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(400, response.status_code)
