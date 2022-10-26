from django.contrib import admin
from django.urls import path
from .views import books_list, book_details, authors_list, author_details, borrowed

app_name = "books"
urlpatterns = [
    path('', books_list, name='books_list'),
    path('books/<int:id>', book_details, name='book_details'),
    path('authors_list/', authors_list, name='authors_list'),
    path('author_details/<int:id>', author_details, name='author_details'),
    path('borrowed/<int:id>', borrowed, name='borrowed'),
]
