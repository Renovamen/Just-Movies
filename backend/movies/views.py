from django.db.models import Q

from .models import Movie

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializer import MovieSerializer


MOVIES_PER_PAGE = 15
simple_query = None
text = None
genre = None
year_period = None
rating_average = None

@api_view(['GET'])
def movie_list(request, page_id):
    page_id = int(page_id)
    page_size = 10

    movies = Movie.objects.all()

    start = (page_id - 1) * page_size
    end = len(movies) if (start + page_size >= len(movies)) else start + page_size

    serializer = MovieSerializer(movies[start:end], many=True)

    context = {
        'movies': serializer.data,
        'total': len(movies),
    }

    return Response(data = context, status = status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail(request, movie_id):

    movie = Movie.objects.get(id = movie_id)
    serializer = MovieSerializer(movie)

    return Response(data = serializer.data, status = status.HTTP_200_OK)


@api_view(['GET'])
def get_search(request, text):

    movies = Movie.objects.filter(Q(title__exact = text) | Q(title__icontains = text) | Q(aka__icontains = text))
    serializer = MovieSerializer(movies[:100], many = True)

    context = {
        'movies': serializer.data,
    }

    return Response(data = context, status = status.HTTP_200_OK)


@api_view(['GET'])
def get_category(request, genre, country, page_id):

    if(genre != '全部类型' and country != '全部地区'):
        movies = Movie.objects.filter(genres__genre = genre, countries__country = country)
    elif(genre == '全部类型' and country == '全部地区'):
        movies = Movie.objects.all()
    elif(genre == '全部类型'):
        movies = Movie.objects.filter(countries__country = country)
    elif(country == '全部地区'):
        movies = Movie.objects.filter(genres__genre = genre)

    page_id = int(page_id)
    page_size = 20
    start = (page_id - 1) * page_size
    end = len(movies) if (start + page_size >= len(movies)) else start + page_size

    serializer = MovieSerializer(movies[start:end], many=True)

    context = {
        'movies': serializer.data,
        'total': len(movies),
    }

    return Response(data = context, status = status.HTTP_200_OK)
