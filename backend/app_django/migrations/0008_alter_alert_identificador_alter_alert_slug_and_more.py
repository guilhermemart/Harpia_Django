# Generated by Django 4.0.1 on 2022-01-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0007_alter_alert_identificador_alter_alert_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='identificador',
            field=models.CharField(default=1643223416689, max_length=255),
        ),
        migrations.AlterField(
            model_name='alert',
            name='slug',
            field=models.SlugField(default='alerta_1643223416690'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='timestamp',
            field=models.IntegerField(default=1643223416),
        ),
    ]