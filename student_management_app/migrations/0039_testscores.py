# Generated by Django 4.1.2 on 2023-05-20 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0038_testdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestScores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('test1', models.FloatField(default='0.0')),
                ('test2', models.FloatField(default='0.0')),
                ('test3', models.FloatField(default='0.0')),
                ('final', models.FloatField(default='0.0')),
                ('attendance', models.FloatField(default='0.0')),
                ('subject_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.subjects', to_field='subject_code')),
                ('usn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'unique_together': {('subject_code', 'usn')},
            },
        ),
    ]
