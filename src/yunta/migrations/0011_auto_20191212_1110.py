# Generated by Django 3.0 on 2019-12-12 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yunta', '0010_auto_20191212_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='junta',
            old_name='name',
            new_name='nombre',
        ),
    ]