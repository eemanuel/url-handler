from django.contrib.auth.models import User
from django.db import models
from core_utils.models import TimeStampModel


class UserProfile(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'username:' + self.user.username + ' id:' + str(self.id)
