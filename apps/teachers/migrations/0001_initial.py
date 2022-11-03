# Generated by Django 4.1.2 on 2022-11-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachers_jobtitle', models.CharField(choices=[('TEAC', 'Teacher'), ('HTCH', 'Head Teacher'), ('DIRE', 'Director')], default='TEAC', max_length=4)),
                ('photo', models.ImageField(upload_to='teachers/')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
    ]
