from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'favorite_genres')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        favorite_genres = validated_data.pop('favorite_genres', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        if favorite_genres:
            user.favorite_genres = favorite_genres
            user.save()
        return user
