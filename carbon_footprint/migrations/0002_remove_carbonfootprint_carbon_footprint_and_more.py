# Generated by Django 4.0.4 on 2023-04-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_footprint', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbonfootprint',
            name='carbon_footprint',
        ),
        migrations.AddField(
            model_name='carbonfootprint',
            name='airplane',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='carbonfootprint',
            name='biking',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='carbonfootprint',
            name='bus',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='carbonfootprint',
            name='car_diesel',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='carbonfootprint',
            name='car_electric',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='carbonfootprint',
            name='car_gasoline',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='carbonfootprint',
            name='train',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='carbonfootprint',
            name='walking',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='carbonfootprint',
            name='distance',
            field=models.FloatField(default=0.0),
        ),
    ]
