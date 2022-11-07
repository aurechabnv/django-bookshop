from django.contrib import admin

from store.models import Author, Genre, Book, Review

# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Review)
