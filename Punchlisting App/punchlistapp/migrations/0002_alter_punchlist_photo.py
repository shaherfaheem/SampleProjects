# Generated by Django 5.0.6 on 2024-06-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punchlistapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punchlist',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
