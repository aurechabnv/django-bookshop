from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Auteur"


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    isbn13 = models.CharField(unique=True, blank=False, max_length=13)
    isbn10 = models.CharField(unique=True, blank=False, max_length=10)
    cover = models.ImageField(blank=True)
    published_date = models.DateField(blank=True)
    publisher = models.CharField(blank=True, max_length=128)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    # TODO: number_of_stars computed from reviews

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Livre"


class Review(models.Model):
    number_of_stars = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    reviewer = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='reviews', related_query_name='review')
    reviewed_item = models.ForeignKey(Book, on_delete=models.CASCADE,
                                      related_name='reviews', related_query_name='review')
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.number_of_stars}/5, {self.reviewed_item}"

    class Meta:
        verbose_name = "Avis"
        verbose_name_plural = "Avis"
