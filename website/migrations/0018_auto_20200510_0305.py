# Generated by Django 3.0.4 on 2020-05-10 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_pedido_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='email',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(default='Criado', max_length=300),
        ),
    ]