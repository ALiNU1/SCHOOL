from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 100)
    password = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
