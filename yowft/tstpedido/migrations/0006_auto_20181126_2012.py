# Generated by Django 2.1.2 on 2018-11-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tstpedido', '0005_remove_produto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='id',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nm_categoria',
            field=models.CharField(max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf_cnpj',
            field=models.CharField(max_length=14, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='especie',
            name='nm_especie',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='cd_produto',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
    ]
