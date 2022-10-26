from django.test import TestCase
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm


class PostFormTest(TestCase):

    def setUp(self):
        Author.objects.create(nick='t_testowy', email='test.testowy@hogwarts.com', bio='test bio')
        self.a1 = Author.objects.get(nick='t_testowy')

    def DataBaseObjectsNumber(self):
        self.assertEqual(len(Post.objects.all()), 0)

    def DataBaseObjectsId(self, x):
        self.assertEqual(x.id, 1)

    def test_post_save_correct_data_value(self):
        data = {'title': 'title test', 'content': 'content test',
                'author_id': self.a1}
        self.DataBaseObjectsNumber()
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        Post.objects.get_or_create(**form.cleaned_data)
        p = Post.objects.get(title=data['title'], content=data['content test'], author_id=data['author_id'])
        self.assertIsInstance(p, Post)
        self.DataBaseObjectsId(p)
        self.assertEqual(p.content, 'content test')


class AuthorFormTest(TestCase):

    def DataBaseObjectsNumber(self):
        self.assertEqual(len(Author.objects.all()), 0)

    def DataBaseObjectsId(self, x):
        self.assertEqual(x.id, 1)

    def test_author_save_correct_data_value(self):
        data = {'nick': 't_testowy', 'email': 'test.testowy@hogwarts.com', 'bio': 'test bio'}
        self.DataBaseObjectsNumber()
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Author)
        self.DataBaseObjectsId(r)
        self.assertEqual(r.bio, 'test bio')
