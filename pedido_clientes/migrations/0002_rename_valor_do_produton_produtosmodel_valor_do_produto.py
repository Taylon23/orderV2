# Generated by Django 4.2.7 on 2024-03-13 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido_clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produtosmodel',
            old_name='valor_do_produton',
            new_name='valor_do_produto',
        ),
    ]
