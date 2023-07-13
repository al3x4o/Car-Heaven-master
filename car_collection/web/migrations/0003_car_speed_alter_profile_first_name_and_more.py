# Generated by Django 4.2.3 on 2023-07-12 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='speed',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(6, message='Must contain at LEAST 6 symbols')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2, message='The username must be a minimum of 2 chars')]),
        ),
    ]
