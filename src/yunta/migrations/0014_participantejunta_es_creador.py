# Generated by Django 3.0 on 2019-12-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yunta', '0013_auto_20191213_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantejunta',
            name='es_creador',
            field=models.BooleanField(default=False),
        ),
    ]
