from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('movies.urls', 'movies'), namespace='movies')),
    path(r'', TemplateView.as_view(template_name = "index.html")) # 调打包好的模板
]
