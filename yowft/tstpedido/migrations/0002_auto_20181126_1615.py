# Generated by Django 2.1.2 on 2018-11-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tstpedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='telefone_contato',
            field=models.CharField(max_length=11),
        ),
    ]
