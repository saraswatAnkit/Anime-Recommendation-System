from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from anime.models import Anime
from .models import UserPreference
from django.shortcuts import get_object_or_404

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully!'})
        return Response(serializer.errors, status=400)

class ManagePreferencesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'favorite_genres': user.favorite_genres,
            'watched_animes': [anime.name for anime in user.watched_animes.all()]
        })

    def post(self, request):
        favorite_genres = request.data.get('favorite_genres', [])
        watched_animes = request.data.get('watched_animes', [])

        user = request.user
        # Get or create UserPreference for the current user
        user_preference, created = UserPreference.objects.get_or_create(user=user)
        user_preference.favorite_genres = favorite_genres
        user_preference.save()

        if watched_animes:
            for anime_id in watched_animes:
                anime = get_object_or_404(Anime, id=anime_id)
                user.watched_animes.add(anime)

        return Response({'message': 'Preferences updated successfully!'})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh', None)
        if not refresh_token:
            return Response({'error': 'Refresh token is required.'}, status=400)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successfully logged out!'})
        except AttributeError:
            return Response({'error': 'Blacklist feature not enabled.'}, status=501)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
