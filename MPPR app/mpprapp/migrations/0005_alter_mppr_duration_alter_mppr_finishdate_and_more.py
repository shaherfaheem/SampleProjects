# Generated by Django 5.0.6 on 2024-06-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpprapp', '0004_alter_mppr_duration_alter_mppr_finishdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mppr',
            name='duration',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='mppr',
            name='finishdate',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='mppr',
            name='rateHourPerSqm',
            field=models.FloatField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='mppr',
            name='startdate',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]