# Generated by Django 3.0.4 on 2020-05-05 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
