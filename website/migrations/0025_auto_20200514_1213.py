# Generated by Django 3.0.4 on 2020-05-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_auto_20200514_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resposta',
            name='status',
        ),
        migrations.AlterField(
            model_name='resposta',
            name='pedido',
            field=models.CharField(max_length=5),
        ),
    ]