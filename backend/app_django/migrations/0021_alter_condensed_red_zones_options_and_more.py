# Generated by Django 4.0.1 on 2022-01-30 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0020_alter_alert_identificador_alter_alert_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condensed_red_zones',
            options={'ordering': ('-date_added',), 'verbose_name_plural': 'condensed_red_zone'},
        ),
        migrations.AlterField(
            model_name='alert',
            name='identificador',
            field=models.CharField(default=1643578834273, max_length=255),
        ),
        migrations.AlterField(
            model_name='alert',
            name='slug',
            field=models.SlugField(default='alerta_1643578834273'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='timestamp',
            field=models.IntegerField(default=1643578834),
        ),
        migrations.AlterField(
            model_name='condensed_red_zones',
            name='identificador',
            field=models.CharField(default=1643578834275, max_length=255),
        ),
        migrations.AlterField(
            model_name='condensed_red_zones',
            name='red_zones_txt',
            field=models.FileField(upload_to='uploads/red_zones/<django.db.models.query_utils.DeferredAttribute object at 0x7fbb28e31bb0>/condensed'),
        ),
        migrations.AlterField(
            model_name='condensed_red_zones',
            name='slug',
            field=models.SlugField(default='condensed_red_zones_None_1643578834'),
        ),
        migrations.AlterField(
            model_name='condensed_red_zones',
            name='timestamp',
            field=models.IntegerField(default=1643578834),
        ),
        migrations.AlterField(
            model_name='red_zone',
            name='dots_txt',
            field=models.FileField(upload_to='uploads/red_zones/<django.db.models.query_utils.DeferredAttribute object at 0x7fbb28e31bb0>'),
        ),
        migrations.AlterField(
            model_name='red_zone',
            name='identificador',
            field=models.CharField(default=1643578834274, max_length=255),
        ),
        migrations.AlterField(
            model_name='red_zone',
            name='slug',
            field=models.SlugField(default='red_zone_<django.db.models.query_utils.DeferredAttribute object at 0x7fbb28e31bb0>_1643578834274'),
        ),
        migrations.AlterField(
            model_name='red_zone',
            name='timestamp',
            field=models.IntegerField(default=1643578834),
        ),
    ]
