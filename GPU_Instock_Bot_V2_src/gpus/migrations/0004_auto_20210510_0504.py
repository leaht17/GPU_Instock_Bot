# Generated by Django 3.2 on 2021-05-10 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpus', '0003_gpu_alias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpu',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='model',
        ),
    ]
