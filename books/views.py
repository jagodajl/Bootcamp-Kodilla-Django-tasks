from importlib.resources import is_resource
from random import choices
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from books.models import Book, Author, Borrow
from books.forms import BookForm, AuthorForm, BorrowedForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def borrowed(request, id):
    if request.method == "POST":
        form = request.POST
        print(f'*******{form}************')
        book = Borrow.objects.get(book_id=form['book_id'])
        book.is_returned = True
        book.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Book returned.")

    borrowed = Borrow.objects.filter(user_id=id, is_returned=False)
    books = Book.objects.all()

    print("############")
    print(borrowed)

    return render(
        request=request,
        template_name="books/borrowed_books.html",
        context={"books": books, "borrowed": borrowed}
    )


def book_details(request, id):
    if request.method == "POST":
        form = request.POST
        print(f'*******{form}************')

        borrowed = Borrow.objects.get_or_create(book_id=id, user_id=form['user_id'], is_returned=True)

        borrowed[0].is_returned = False
        borrowed[0].save()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Book borrowed. Go to your list of boorowed book to return.")

    book = Book.objects.get(id=id)
    author = Author.objects.get(id=book.author_id)
    try:
        borrowed = Borrow.objects.get(book_id=id)
        if borrowed and borrowed.is_returned == False:
            print("jest w ifie")
            available = False
        else:
            available = True
            print("jest w excepcie")
    except:
        available = True

    return render(
        request=request,
        template_name="books/book_details.html",
        context={"book": book, "author": author, "available": available}
    )


@login_required
def books_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="books/books_list.html",
        context={
            "books": books,
        }
    )


def author_details(request, id):
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author_id=id)

    return render(
        request=request,
        template_name="books/author_details.html",
        context={"author": author, "books": books}
    )


def authors_list(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 5)
    page_number = request.GET.get('page')
    authors = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="books/authors_list.html",
        context={
            "authors": authors,
        }
    )
