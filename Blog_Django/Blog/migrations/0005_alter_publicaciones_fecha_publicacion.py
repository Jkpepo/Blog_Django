# Generated by Django 5.1.2 on 2024-11-19 01:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_publicaciones_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha_publicacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]