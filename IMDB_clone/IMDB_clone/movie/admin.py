from django.contrib import admin

from IMDB_clone.movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
