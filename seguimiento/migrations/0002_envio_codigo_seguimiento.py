# Generated by Django 4.1.2 on 2023-07-03 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='codigo_seguimiento',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
