from django.urls import path
from .views import AnimeSearchView, AnimeRecommendationView

urlpatterns = [
    path('search/', AnimeSearchView.as_view(), name='anime-search'),
    path('recommendations/', AnimeRecommendationView.as_view(), name='anime-recommendations'),
]
