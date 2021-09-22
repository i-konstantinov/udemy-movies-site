
from django.views.generic import ListView, DetailView

from IMDB_clone.movie.models import Movie, MovieLinks


class ListMovies(ListView):
    model = Movie
    template_name = 'list_movies.html'
    context_object_name = 'movies'
    paginate_by = 2


class MovieDetails(DetailView):
    model = Movie
    template_name = 'movie_details.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        return context


class MovieCategory(ListView):
    model = Movie
    template_name = 'list_movies.html'

    def get_queryset(self):
        search_query = self.request.GET.get('choice')
        wanted_category = None
        for cat in self.model.CATEGORY_CHOICES:
            if cat[1] == search_query:
                wanted_category = cat[0]
                break
        movies = Movie.objects.filter(category=wanted_category)
        return movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = self.get_queryset()
        return context
