# Generated by Django 4.0.1 on 2022-01-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0003_user_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='thumb_down',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alert',
            name='thumb_up',
            field=models.BooleanField(default=False),
        ),
    ]
