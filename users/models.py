from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUser(AbstractUser):
    GENDERS = (
            ('m', 'Male'),
            ('f', 'Female')
            )
    fio = models.CharField('Fullname', max_length=255, default='')
    gender = models.CharField('Sex', max_length=1, choices=GENDERS, default='')

    def __str__(self):
        return self.username

