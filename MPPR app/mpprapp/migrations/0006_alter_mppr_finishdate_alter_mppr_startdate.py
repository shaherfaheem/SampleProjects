# Generated by Django 5.0.6 on 2024-06-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpprapp', '0005_alter_mppr_duration_alter_mppr_finishdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mppr',
            name='finishdate',
            field=models.DateField(blank=True, default='00/00/0000', null=True),
        ),
        migrations.AlterField(
            model_name='mppr',
            name='startdate',
            field=models.DateField(blank=True, default='00/00/0000', null=True),
        ),
    ]
