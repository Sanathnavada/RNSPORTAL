# Generated by Django 4.1.7 on 2023-04-03 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0004_subjects_subject_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionYearModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('session_start_year', models.DateField()),
                ('session_end_year', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='students',
            name='session_end_year',
        ),
        migrations.RemoveField(
            model_name='students',
            name='session_start_year',
        ),
        migrations.AddField(
            model_name='attendance',
            name='session_year_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.sessionyearmodel'),
        ),
        migrations.AddField(
            model_name='students',
            name='session_year_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.sessionyearmodel'),
        ),
    ]
