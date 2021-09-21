from django.db import models


class Movie(models.Model):
    CATEGORY_CHOICE_ACTION = 'A'
    CATEGORY_CHOICE_DRAMA = 'D'
    CATEGORY_CHOICE_COMEDY = 'C'
    CATEGORY_CHOICE_ROMANCE = 'R'
    CATEGORY_CHOICES = (
        (CATEGORY_CHOICE_ACTION, 'Action'),
        (CATEGORY_CHOICE_DRAMA, 'Drama'),
        (CATEGORY_CHOICE_COMEDY, 'Comedy'),
        (CATEGORY_CHOICE_ROMANCE, 'Romance'),
    )

    LANGUAGE_CHOICE_ENGLISH = 'ENG'
    LANGUAGE_CHOICE_GERMAN = 'GER'
    LANGUAGE_CHOICES = (
        (LANGUAGE_CHOICE_ENGLISH, 'English'),
        (LANGUAGE_CHOICE_GERMAN, 'German'),
    )

    STATUS_CHOICE_RECENTLY_ADDED = 'RA'
    STATUS_CHOICE_MOST_WATCHED = 'MW'
    STATUS_CHOICE_TOP_RATED = 'TR'
    STATUS_CHOICES = (
        (STATUS_CHOICE_RECENTLY_ADDED, 'Recently Added'),
        (STATUS_CHOICE_MOST_WATCHED, 'Most Watched'),
        (STATUS_CHOICE_TOP_RATED, 'Top Rated'),
    )

    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=1,
    )

    title = models.CharField(
        max_length=100,
    )

    cast = models.CharField(
        default='',
        max_length=500,
    )

    description = models.TextField(
        max_length=10000,
    )

    image = models.ImageField(
        upload_to='movies',
    )

    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=3,
    )

    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=2,
    )

    year_of_production = models.DateField()

    view_count = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return self.title


class MovieLinks(models.Model):
    LINK_TYPE_CHOICES = (
        ('D', 'download link'),
        ('W', 'watch link'),
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )
    type_of_link = models.CharField(
        choices=LINK_TYPE_CHOICES,
        max_length=1,
    )
    link = models.URLField()

    def __str__(self):
        return f"{self.movie} {self.type_of_link} link"

# tags
