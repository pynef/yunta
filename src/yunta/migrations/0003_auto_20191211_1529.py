# Generated by Django 3.0 on 2019-12-11 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yunta', '0002_junta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['dni'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='user',
        ),
    ]