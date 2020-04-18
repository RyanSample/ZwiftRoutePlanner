# Generated by Django 3.0.5 on 2020-04-18 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('world_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('world', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routeplanner.World')),
            ],
        ),
    ]
