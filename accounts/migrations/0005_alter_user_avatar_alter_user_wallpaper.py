# Generated by Django 5.0.1 on 2024-06-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_ongoing_fictions_user_ongoing_chapters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar_new.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='wallpaper',
            field=models.ImageField(default='wallpaper_default.jpeg', null=True, upload_to=''),
        ),
    ]
