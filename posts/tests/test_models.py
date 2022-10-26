from django.test import TestCase
from posts.models import Post, Author


class PostAuthorModelTest(TestCase):
    def setUp(self):
        Author.objects.create(nick='t_testowy', email='test.testowy@hogwarts.com', bio='test bio')
        self.a1 = Author.objects.get(nick='t_testowy')
        Post.objects.create(title='title test', content='content test', author_id=1)

    def test_author(self):
        self.assertEqual(str(self.a1), 'nick: t_testowy, email: test.testowy@hogwarts.com, bio: test bio')

    def test_post(self):
        p1 = Post.objects.get(author_id=self.a1)

        self.assertEqual(str(p1.title), 'title test')
        self.assertEqual(str(p1.content), 'content test')
        self.assertEqual(str(p1.author_id), 'nick: t_testowy, email: test.testowy@hogwarts.com, bio: test bio')
