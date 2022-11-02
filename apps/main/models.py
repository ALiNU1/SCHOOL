from django.db import models

# Create your models here.
class News(models.Model):
    description = models.TextField()
    photo = models.ImageField(upload_to='news/')
    name = models.CharField(max_length = 255)
    rate = models.IntegerField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
