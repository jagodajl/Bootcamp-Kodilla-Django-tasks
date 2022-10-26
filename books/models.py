from django.db import models
from django.forms import BooleanField, CharField, ImageField, IntegerField
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    number_of_pages = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='photos/%Y/%m/%d', null=True)
    author = models.ForeignKey(
        'books.Author',
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    def __str__(self):
        return f"id:{self.id}, title={self.title}, description={self.description}, number_of_pages={self.title}, added={self.added}, author={self.author}"

    tags = models.ManyToManyField("books.Tag", related_name="books", )


class Author(models.Model):
    name = models.CharField(max_length=30, unique=False)
    lastname = models.CharField(max_length=20, unique=False)
    nick = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"id:{self.id}, name={self.name}, nick={self.nick}"


class Borrow(models.Model):
    borrowed_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now=True)
    is_returned = models.BooleanField()
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"id:{self.id}, is_returned={self.is_returned}, book_id={self.book.id}, user_id={self.user}"


class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
