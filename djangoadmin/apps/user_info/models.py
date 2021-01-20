from django.db import models

from djangoadmin.apps.user_info.constants import GENDER_CHOICES


class UserInfo(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    company = models.CharField(max_length=255)
    bio = models.TextField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
