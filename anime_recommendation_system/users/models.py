from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    favorite_genres = models.JSONField(default=list, blank=True)
    watched_animes = models.ManyToManyField('anime.Anime', related_name='watched_by', blank=True)


class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users_userpreference')
    favorite_genres = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Preferences"

