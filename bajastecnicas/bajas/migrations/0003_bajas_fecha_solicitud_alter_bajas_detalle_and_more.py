# Generated by Django 5.1.3 on 2024-12-03 19:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bajas', '0002_alter_bajas_inm_herramienta_alter_bajas_no_inv'),
    ]

    operations = [
        migrations.AddField(
            model_name='bajas',
            name='fecha_solicitud',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bajas',
            name='detalle',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bajas',
            name='valor_residual',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
