from django.views.generic import ListView, DetailView

from IMDB_clone.movie.models import Movie, MovieLinks


class ListMovies(ListView):
    model = Movie
    template_name = 'list_movies.html'
    paginate_by = 3


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
        category_choice = self.request.GET.get('category_choice')
        movies = Movie.objects.filter(category=category_choice)
        return movies


class MovieLanguage(ListView):
    model = Movie
    template_name = 'list_movies.html'

    def get_queryset(self):
        language_choice = self.request.GET.get('language_choice')
        movies = Movie.objects.filter(language=language_choice)
        return movies
