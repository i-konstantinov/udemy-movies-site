from django.shortcuts import render
from django.views.generic import ListView, DetailView

from IMDB_clone.movie.models import Movie


# def index(request):
#     context = {
#         'movies': Movie.objects.all(),
#     }
#     return render(request, 'list_movies.html', context)


class ListMovies(ListView):
    model = Movie
    template_name = 'list_movies.html'
    context_object_name = 'movies'
    paginate_by = 1


class MovieDetails(DetailView):
    model = Movie
    template_name = 'movie_details.html'