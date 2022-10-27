from rest_framework import serializers

from books.models import Book, Borrow, Author, Tag

#zadanie2, czesc 1
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'number_of_pages', 'description', 'added', 'cover', 'author', 'tags')

#zadanie2, czesc 1
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'lastname', 'nick')


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ('id', 'is_returned', 'borrowed_date', 'return_date')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'word', 'created')
