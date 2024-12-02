from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('favorite_genres', 'watched_animes')}),
    )
    list_display = ['username', 'email', 'is_staff']

admin.site.register(User, CustomUserAdmin)

