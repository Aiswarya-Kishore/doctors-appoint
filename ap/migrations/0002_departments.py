# Generated by Django 4.2.3 on 2023-11-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depname', models.CharField(max_length=20)),
            ],
        ),
    ]
