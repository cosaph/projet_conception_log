# Generated by Django 5.0.3 on 2024-03-11 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_course_courset'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Courset',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
