# Generated by Django 3.0.4 on 2020-05-10 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_city_hospitalname'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='answers',
            field=models.IntegerField(default=0),
        ),
    ]
