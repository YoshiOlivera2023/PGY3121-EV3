# Generated by Django 4.1.2 on 2023-07-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0003_rename_usuario_pedido_id_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productocarrito',
            name='estado',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
