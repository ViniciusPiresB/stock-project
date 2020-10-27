# Generated by Django 2.2.12 on 2020-10-27 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20191005_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='ncm',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='preço de saida'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='preço de custo'),
        ),
    ]
