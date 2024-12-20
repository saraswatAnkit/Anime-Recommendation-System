# Generated by Django 5.1.3 on 2024-12-02 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_remove_userpreference_watched_animes_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreference',
            name='watched_animes',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='favorite_genres',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to=settings.AUTH_USER_MODEL),
        ),
    ]
