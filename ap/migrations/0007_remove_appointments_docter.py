# Generated by Django 4.2.3 on 2023-11-06 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0006_logintb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='docter',
        ),
    ]
