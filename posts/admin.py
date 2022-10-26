from django.contrib import admin

from django.contrib import admin
from posts.models import Post, Author, Tag


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created", "modified"]
    list_filter = ["title"]
    search_fields = ["title", "created"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['nick', 'email']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
