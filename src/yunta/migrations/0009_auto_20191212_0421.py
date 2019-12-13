# Generated by Django 3.0 on 2019-12-12 04:21

from django.db import migrations, models
import yunta.models


class Migration(migrations.Migration):

    dependencies = [
        ('yunta', '0008_monedero'),
    ]

    operations = [
        migrations.AddField(
            model_name='junta',
            name='clave',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(default='Profile/default.png', upload_to=yunta.models.generar_ruta_imagen),
        ),
    ]