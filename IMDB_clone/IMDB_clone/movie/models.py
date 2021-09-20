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

    description = models.TextField(
        max_length=1000,
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

    # tags
    # download links
    # watch links
