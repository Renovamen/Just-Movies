import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Just_Movies.settings')

django.setup()

from movies.models import Genre, Country, Person, Movie

def get_data():

    with open('films_all.json', 'rb') as f:
        movie_list = json.load(f)

    for data in movie_list:

        languages = ' / '.join(data['languages'])
        aka = ' / '.join(data['aka'])
        pubdate = ' / '.join(data['pubdate'])

        movie = Movie.objects.create(
            id = data['_id'],
            pubdate = pubdate,
            year = data['year'],
            title = data['title'],
            poster = data['poster'],
            summary = data['summary'],
            languages = languages,
            duration = data['duration'],
            aka = aka,
            stars1 = data['rating']["stars"][4] if len(data['rating']["stars"]) > 4 else 0,
            stars2 = data['rating']["stars"][3] if len(data['rating']["stars"]) > 3 else 0,
            stars3 = data['rating']["stars"][2] if len(data['rating']["stars"]) > 2 else 0,
            stars4 = data['rating']["stars"][1] if len(data['rating']["stars"]) > 1 else 0,
            stars5 = data['rating']["stars"][0] if len(data['rating']["stars"]) > 0 else 0,
            rating_average = data['rating']["average"],
            rating_people = data['rating']["rating_people"] if data['rating']["rating_people"] != '' else 0,
        )

        for director in data['directors']:
            person, _ = Person.objects.get_or_create(name = director['name'])
            movie.director.add(person)

        for cast in data['casts']:
            person, _ = Person.objects.get_or_create(name = cast['name'])
            movie.casts.add(person)

        for writer in data['writers']:
            person, _ = Person.objects.get_or_create(name = writer['name'])
            movie.writer.add(person)

        for genre in data['genres']:
            genre_object, _ = Genre.objects.get_or_create(genre = genre)
            movie.genres.add(genre_object)

        for country in data['countries']:
            country_object, _ = Country.objects.get_or_create(country = country)
            movie.countries.add(country_object)

        movie.save()


if __name__ == "__main__":

    get_data()
