# Generated by Django 3.0.3 on 2020-02-04 19:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('greenhouse', '0002_sensorvalue_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='temphum',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]