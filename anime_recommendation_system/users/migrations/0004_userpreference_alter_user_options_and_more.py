# Generated by Django 5.1.3 on 2024-12-02 08:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options_user_users_user_email_6f2530_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_genres', models.JSONField(blank=True, default=list)),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveIndex(
            model_name='user',
            name='users_user_email_6f2530_idx',
        ),
        migrations.RemoveField(
            model_name='user',
            name='watched_animes',
        ),
        migrations.AddField(
            model_name='userpreference',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users_userpreference', to=settings.AUTH_USER_MODEL),
        ),
    ]