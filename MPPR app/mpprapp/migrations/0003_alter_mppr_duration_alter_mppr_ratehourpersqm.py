# Generated by Django 5.0.6 on 2024-06-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpprapp', '0002_alter_mppr_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mppr',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mppr',
            name='rateHourPerSqm',
            field=models.FloatField(null=True),
        ),
    ]