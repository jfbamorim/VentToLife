# Generated by Django 3.0.4 on 2020-05-01 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200501_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='datastored',
        ),
        migrations.RemoveField(
            model_name='tecnico',
            name='datastored',
        ),
    ]
