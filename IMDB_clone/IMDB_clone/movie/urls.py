from django.urls import path

from IMDB_clone.movie import views

urlpatterns = [
    path('', views.ListMovies.as_view(), name='list movies'),
    path('details/<int:pk>', views.MovieDetails.as_view(), name='movie details'),
    path('category/', views.MovieCategory.as_view(), name='movie category'),
]
