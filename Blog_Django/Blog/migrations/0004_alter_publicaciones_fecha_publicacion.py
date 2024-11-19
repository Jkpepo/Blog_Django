# Generated by Django 5.1.2 on 2024-11-19 01:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_publicaciones_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha_publicacion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]