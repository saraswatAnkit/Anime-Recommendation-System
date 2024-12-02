# Generated by Django 5.1.3 on 2024-12-02 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_user_watched_animes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['email'], name='users_user_email_6f2530_idx'),
        ),
    ]
