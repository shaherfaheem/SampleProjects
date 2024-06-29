# Generated by Django 5.0.6 on 2024-06-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Punchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('contractor', models.CharField(max_length=50)),
                ('action', models.CharField(max_length=50)),
                ('commitment', models.DateField(blank=True, null=True)),
                ('finishdate', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
