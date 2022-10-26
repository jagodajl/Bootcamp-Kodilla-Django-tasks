from django import forms
from books.models import Book, Author, Borrow


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "number_of_pages", "cover", "author", "tags"]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "lastname", "nick"]


class BorrowedForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ["is_returned", "book", "user"]
