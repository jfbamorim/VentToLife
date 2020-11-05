# Generated by Django 3.0.4 on 2020-05-02 00:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200501_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tecnico',
            name='cae',
        ),
        migrations.RemoveField(
            model_name='tecnico',
            name='nipc',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='phone_number',
            field=models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator(message='O número de telemóvel é inválido.', regex='^\\+?9?\\d{9}$')], verbose_name='Telemovel'),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='phone_number',
            field=models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator(message='O número de telemóvel é inválido.', regex='^\\+?9?\\d{9}$')], verbose_name='Telemovel'),
        ),
    ]
