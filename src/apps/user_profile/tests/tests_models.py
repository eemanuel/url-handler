from django.contrib.auth.models import User
from django.test import TestCase
from user_profile.models import UserProfile


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='cosme')
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_output_user_profile(self):
        self.user_profile_qs = UserProfile.objects.all()
        self.last_user = self.user_profile_qs.last()
        self.assertEqual('username:cosme id:1', self.last_user.__str__())
