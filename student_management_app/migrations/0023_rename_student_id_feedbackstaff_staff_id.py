# Generated by Django 4.1.2 on 2023-05-08 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0022_alter_staffleave_staff_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackstaff',
            old_name='student_id',
            new_name='staff_id',
        ),
    ]
