# Generated by Django 4.1.2 on 2023-05-07 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0013_alter_staff_admin_alter_subjects_subject_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentTestScore',
        ),
    ]
