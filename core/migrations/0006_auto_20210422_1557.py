# Generated by Django 3.2 on 2021-04-22 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210422_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.exercise'),
        ),
        migrations.AddField(
            model_name='workout',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='workout',
            name='set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.set'),
        ),
    ]
