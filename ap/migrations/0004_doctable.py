# Generated by Django 4.2.3 on 2023-11-01 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0003_departments_ndoctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=19)),
                ('departments', models.CharField(max_length=20)),
            ],
        ),
    ]
