# Generated by Django 3.2 on 2021-04-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bodypart', models.CharField(choices=[('Chest', 'Chest'), ('Back', 'Back'), ('Shoulders', 'Shoulders'), ('Arms', 'Arms'), ('Legs', 'Legs'), ('Cardio', 'Cardio')], max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
