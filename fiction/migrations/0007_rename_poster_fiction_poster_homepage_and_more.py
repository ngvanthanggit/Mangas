# Generated by Django 5.0.1 on 2024-06-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiction', '0006_alter_fiction_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fiction',
            old_name='poster',
            new_name='poster_homepage',
        ),
        migrations.AddField(
            model_name='fiction',
            name='poster_fictionpage',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
