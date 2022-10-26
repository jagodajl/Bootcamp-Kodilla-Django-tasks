from random import choices
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm
from django.contrib.auth.decorators import login_required

""" def posts_list(request):
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/list.html",
        context={"posts": posts}
    ) """


def posts_details(request, id):
    post = Post.objects.get(id=id)
    author = Author.objects.get(id=post.author_id_id)
    return render(
        request=request,
        template_name="posts/posts_details.html",
        context={"post": post, "author": author}
    )


@login_required
def posts_list(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(f'*******{form}')
        if form.is_valid():
            print(form.cleaned_data)
            p1 = Post.objects.create(title=form.cleaned_data['title'], content=form.cleaned_data['content'],
                                     author_id=form.cleaned_data['author_id'], image=request.FILES['image'])

            messages.add_message(
                request,
                messages.SUCCESS,
                "New post created!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors
            )

    form = PostForm()
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={
            "posts": posts,
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


def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(data=request.POST)
        print(f'*******{form}')
        if form.is_valid():
            Author.objects.get_or_create(**form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "New Author created!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={
            "authors": authors,
            "form": form
        }
    )
