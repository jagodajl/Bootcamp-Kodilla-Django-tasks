# Create your views here.
from django.shortcuts import render
from django.contrib import messages

from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm


def homepage(request):
    return render(
        request=request,
        template_name="posts/home.html"
    )


def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "You have successfully created a new author."
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )
    elif request.method == "GET":
        form = AuthorForm()
        authors = Author.objects.all()
        return render(
            request=request,
            template_name="posts/authors_list.html",
            context={"authors": authors,
                     "form": form
                     }
        )


def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={"author": author}
    )


def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "You have successfully created a new post!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )
    elif request.method == "GET":
        posts = Post.objects.all()
        form = PostForm()
        return render(
            request=request,
            template_name="posts/posts_list.html",
            context={"posts": posts,
                     "form": form
                     }
        )


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"post": post}
    )
