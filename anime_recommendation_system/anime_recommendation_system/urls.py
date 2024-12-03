from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anime/', include('anime.urls')),
    path('auth/', include('users.urls')),
    path('user/', include('users.urls')),
]
