# Generated by Django 4.2.4 on 2024-03-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido_clientes', '0013_alter_itempedidomodel_referencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedidomodel',
            name='referencia',
            field=models.CharField(choices=[('CX', 'CX'), ('KG', 'Quilo'), ('UN', 'Unidade'), ('FD', 'Fardo')], max_length=10),
        ),
    ]