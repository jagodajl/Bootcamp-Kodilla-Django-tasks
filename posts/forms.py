from django import forms
from posts.models import Author, Post

AUTHORS_CHOICES = ()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author_id", "image", "tags"]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["nick", "email"]
