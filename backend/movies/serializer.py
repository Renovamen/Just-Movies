from rest_framework import serializers
from .models import Movie, Genre, Country, Person, Country

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "name")

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "name")


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "name")

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "genre")

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "country")

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=True)
    genres = GenreSerializer(many=True)
    casts = CastSerializer(many=True)
    writer = WriterSerializer(many=True)
    countries = CountrySerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "pubdate", "title", "poster", "summary", "languages", "duration",
                  "aka", "director", "casts", "writer", "genres", "countries", "rating_people",
                  "rating_average", "year", "stars1", "stars2", "stars3", "stars4", "stars5")

