# Generated by Django 2.1.2 on 2018-11-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tstpedido', '0003_categoria_especie_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='cd_produto',
            field=models.CharField(max_length=9),
        ),
    ]