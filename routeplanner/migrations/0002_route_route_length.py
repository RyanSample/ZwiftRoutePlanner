# Generated by Django 3.0.5 on 2020-04-19 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routeplanner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='route_length',
            field=models.FloatField(default=0.0),
        ),
    ]