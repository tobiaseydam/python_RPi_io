# Generated by Django 2.2.4 on 2019-08-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpio_manager', '0003_auto_20190829_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpiopin',
            name='pin',
            field=models.IntegerField(default=4),
        ),
    ]