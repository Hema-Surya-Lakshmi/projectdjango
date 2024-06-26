# Generated by Django 4.1.12 on 2024-04-24 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fauna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('livingstyle', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='flora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pictures', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='nature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seasons', models.CharField(max_length=100)),
                ('weather', models.ImageField(upload_to='')),
                ('fruit', models.ImageField(upload_to='')),
                ('tempature', models.IntegerField()),
                ('habitat', models.ImageField(upload_to='')),
            ],
        ),
    ]
