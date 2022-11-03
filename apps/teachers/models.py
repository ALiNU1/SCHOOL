from random import choices
from django.db import models

# Create your models here.
class Teachers(models.Model):
    teachers_jobtitle = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to = 'teachers/')
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'