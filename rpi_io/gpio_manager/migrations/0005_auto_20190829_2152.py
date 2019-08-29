# Generated by Django 2.2.4 on 2019-08-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpio_manager', '0004_auto_20190829_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpiopin',
            name='connected',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gpiopin',
            name='device',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='gpiopin',
            name='mqtt_alias',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='gpiopin',
            name='pin',
            field=models.IntegerField(default=0),
        ),
    ]
