# Generated by Django 3.0 on 2019-12-13 09:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yunta', '0015_auto_20191213_0926'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participantejunta',
            unique_together={('junta', 'participante')},
        ),
    ]
