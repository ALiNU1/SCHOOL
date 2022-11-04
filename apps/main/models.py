from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    photo = models.ImageField(upload_to='news/')
    name = models.CharField(max_length = 255)
    rate = models.IntegerField()
    duration = models.CharField(blank = True, null=True,max_length = 100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class About(models.Model):
    title = models.CharField(max_length =255)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'about/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

