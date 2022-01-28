# Generated by Django 4.0.1 on 2022-01-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0004_alert_thumb_down_alert_thumb_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='local_image_url',
            field=models.TextField(default='uploads/sauron_imagens/n_avaliadas'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='firebase_image_url',
            field=models.TextField(default='replace_here_later_for_firebase_url'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/sauron_imagens/n_avaliadas'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='alert',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/sauron_thumbnails/'),
        ),
    ]
