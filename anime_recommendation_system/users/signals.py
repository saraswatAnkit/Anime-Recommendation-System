from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from anime.models import UserPreference

@receiver(post_save, sender=User)
def save_user_preference(sender, instance, created, **kwargs):
    if created:
        UserPreference.objects.create(user=instance)
    instance.preferences.save()

    instance.userpreference.save()
