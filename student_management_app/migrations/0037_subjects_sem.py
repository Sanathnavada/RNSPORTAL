# Generated by Django 4.1.2 on 2023-05-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0036_adminhod_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='sem',
            field=models.IntegerField(default=0),
        ),
    ]
