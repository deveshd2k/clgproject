# Generated by Django 2.2.6 on 2019-10-26 13:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0006_auto_20191026_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='private_key',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='enc_field',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='None', max_length=200), size=None), default=list, size=None),
        ),
    ]