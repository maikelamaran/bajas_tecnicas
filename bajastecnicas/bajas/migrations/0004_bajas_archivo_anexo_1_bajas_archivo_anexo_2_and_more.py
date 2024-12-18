# Generated by Django 5.1.3 on 2024-12-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bajas', '0003_bajas_fecha_solicitud_alter_bajas_detalle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bajas',
            name='archivo_anexo_1',
            field=models.FileField(blank=True, null=True, upload_to='anexos/'),
        ),
        migrations.AddField(
            model_name='bajas',
            name='archivo_anexo_2',
            field=models.FileField(blank=True, null=True, upload_to='anexos/'),
        ),
        migrations.AddField(
            model_name='bajas',
            name='archivo_anexo_3',
            field=models.FileField(blank=True, null=True, upload_to='anexos/'),
        ),
        migrations.AddField(
            model_name='bajas',
            name='archivo_anexo_a',
            field=models.FileField(blank=True, null=True, upload_to='anexos/'),
        ),
        migrations.AddField(
            model_name='bajas',
            name='archivo_mov_aft',
            field=models.FileField(blank=True, null=True, upload_to='anexos/'),
        ),
        migrations.AlterField(
            model_name='bajas',
            name='anexo_a',
            field=models.CharField(default='falta', max_length=100),
        ),
        migrations.AlterField(
            model_name='bajas',
            name='anexo_a1',
            field=models.CharField(default='falta', max_length=100),
        ),
        migrations.AlterField(
            model_name='bajas',
            name='anexo_a2',
            field=models.CharField(default='falta', max_length=100),
        ),
        migrations.AlterField(
            model_name='bajas',
            name='anexo_a3',
            field=models.CharField(default='falta', max_length=100),
        ),
        migrations.AlterField(
            model_name='bajas',
            name='mov_aft',
            field=models.CharField(default='falta', max_length=100),
        ),
        migrations.AlterField(
            model_name='bajas',
            name='observaciones',
            field=models.TextField(blank=True),
        ),
    ]
