# Generated by Django 4.1.2 on 2023-06-27 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_met_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_metodo_pago', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('monto_total', models.IntegerField()),
                ('fecha_pago', models.DateField()),
                ('id_met_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagos.metodopago')),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.pedido')),
            ],
        ),
    ]