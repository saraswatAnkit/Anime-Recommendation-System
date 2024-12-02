import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Anime, UserPreference


class AnimeSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.GET.get('query', '')
        genre = request.GET.get('genre', '')

        if not query:
            return Response({'error': 'Query parameter is required'}, status=400)

        query_string = """
        query ($search: String, $genre: String) {
          Media(search: $search, type: ANIME, genre: $genre) {
            title {
              romaji
            }
            genres
            description
            coverImage {
              medium
            }
          }
        }
        """
        variables = {'search': query, 'genre': genre}

        try:
            response = requests.post('https://graphql.anilist.co', json={'query': query_string, 'variables': variables})
            response.raise_for_status()
            data = response.json()

            
            print("Response data:", data)

            if not data or 'data' not in data or 'Media' not in data['data']:
                return Response({'error': 'Invalid response structure from the external API'}, status=500)

            anime_list = data['data']['Media']

            
            if isinstance(anime_list, dict):
                anime_list = [anime_list]  

            results = []
            for anime in anime_list:
                title = anime['title']
                if isinstance(title, dict):
                    title_romaji = title.get('romaji', 'No Title Available')
                else:
                    title_romaji = title

                results.append({
                    'title': title_romaji,
                    'genres': anime['genres'],
                    'description': anime['description'],
                    'image_url': anime['coverImage']['medium']
                })

            return Response(results)

        except requests.exceptions.RequestException as e:
            return Response({'error': f'Failed to fetch data from the external API: {str(e)}'}, status=500)


class AnimeRecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        genre = request.GET.get('genre')
        user_id = request.GET.get('user_id')


        print(f"Received genre: {genre}, user_id: {user_id}")

        if not genre:
            return Response({'error': "The 'genre' parameter is required."}, status=400)
        if not user_id:
            return Response({'error': "The 'user_id' parameter is required."}, status=400)

        
        try:
            recommendations = self.get_recommendations(genre, user_id)
            return Response(recommendations)

        except ValidationError as ve:
            print(f"Validation error: {ve}")
            return Response({'error': str(ve)}, status=400)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return Response({'error': str(e)}, status=500)

    def get_recommendations(self, genre, user_id):
        print(f"Fetching recommendations for genre: {genre} and user_id: {user_id}")

        try:
            user_preferences = UserPreference.objects.get(user_id=user_id)

            
            print(f"User preferences for user_id {user_id}: {user_preferences}")

            
            if genre in user_preferences.favorite_genres:
                recommendations = Anime.objects.filter(genre=genre)
            else:
                recommendations = Anime.objects.filter(genre__in=user_preferences.favorite_genres)

            print(f"Found {len(recommendations)} recommendations for genre {genre}")

            if not recommendations:
                print(f"No anime found for genre: {genre}")
                return {'message': f"No recommendations found for genre: {genre}"}

            
            return recommendations.values('name', 'genre', 'description', 'image_url')

        except UserPreference.DoesNotExist:
            raise ValidationError(f"User preferences not found for user_id {user_id}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
