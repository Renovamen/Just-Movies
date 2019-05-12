from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('getMovieList/<page_id>', views.movie_list),
    path('getMovie/<movie_id>', views.movie_detail),
    path('getCategory/<genre>/<country>/<page_id>', views.get_category),
    path('getSearch/<text>', views.get_search),
]
