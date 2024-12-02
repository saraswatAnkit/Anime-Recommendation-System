from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Anime(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
    
class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    favorite_genres = models.JSONField(default=list)
    watched_animes = models.JSONField(default=list)

    def __str__(self):
        return f"{self.user.username}'s Anime Preferences"