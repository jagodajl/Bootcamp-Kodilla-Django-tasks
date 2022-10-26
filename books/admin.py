from django.contrib import admin

from django.contrib import admin
from books.models import Book, Author, Borrow, Tag


# Register your models here.

@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "number_of_pages", "added", "cover", "author"]
    list_filter = ["title"]
    search_fields = ["title", "created"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'nick']


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['is_returned', 'book', 'user', 'borrowed_date']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
