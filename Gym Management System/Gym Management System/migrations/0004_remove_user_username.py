# Generated by Django 3.1.6 on 2021-12-13 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20211212_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
