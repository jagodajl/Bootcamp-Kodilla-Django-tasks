from rest_framework.viewsets import ModelViewSet

from books.models import Book, Author, Borrow
from books.serializers import BookSerializer, AuthorSerializer, BorrowSerializer


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#zadanie2, czesc 1
class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BorrowViewset(ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
