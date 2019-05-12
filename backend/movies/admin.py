from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Movie


class MovieResource(resources.ModelResource):
    class Meta:
        model = Movie


class MovieModelAdmin(ImportExportModelAdmin):
    resource_class = MovieResource
    list_display = ['title', 'pubdate', 'rating_average']
    list_filter = ['rating_average', 'pubdate', 'genres']
    search_fields = ['title', 'summary']

    class Meta:
        model = Movie


admin.site.register(Movie, MovieModelAdmin)