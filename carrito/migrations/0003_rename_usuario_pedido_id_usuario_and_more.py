# Generated by Django 4.1.2 on 2023-07-06 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_remove_usuario_id_comuna_remove_usuario_id_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='usuario',
            new_name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='productocarrito',
            name='id_carrito',
        ),
        migrations.AddField(
            model_name='productocarrito',
            name='id_usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='carrito.usuario'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
    ]
