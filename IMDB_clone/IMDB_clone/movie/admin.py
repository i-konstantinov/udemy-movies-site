from django.contrib import admin

from IMDB_clone.movie.models import Movie, MovieLinks


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieLinks)
class MovieLinksAdmin(admin.ModelAdmin):
    pass
