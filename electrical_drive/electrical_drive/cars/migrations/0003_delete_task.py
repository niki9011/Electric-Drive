# Generated by Django 3.1.4 on 2023-08-01 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]