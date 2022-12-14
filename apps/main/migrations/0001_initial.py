# Generated by Django 4.1.2 on 2022-11-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='news/')),
                ('name', models.CharField(max_length=255)),
                ('rate', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
