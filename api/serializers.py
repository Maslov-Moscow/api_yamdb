from rest_framework import serializers

from api.models import Genres
from api.models import Titles
from api.models import Categories


class GenreSerialiser(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    class Meta:
        fields = ('name', 'slug')
        model = Genres


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    class Meta:
        fields = ('name', 'slug')
        model = Categories


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerialiser(many=True, required=False, read_only=True)
    category = CategorySerializer(required=False, read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Titles