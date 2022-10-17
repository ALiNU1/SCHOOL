from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')
    phome = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
