# Generated by Django 4.2.3 on 2023-11-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0004_doctable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='ndoctors',
            field=models.IntegerField(),
        ),
    ]
