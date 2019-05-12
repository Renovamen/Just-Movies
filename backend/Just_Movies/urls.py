from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('movies.urls', 'movies'), namespace='movies')),
]
