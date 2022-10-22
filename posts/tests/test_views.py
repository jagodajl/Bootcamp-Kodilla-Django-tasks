from django.test import TestCase
from posts.models import Post, Author


class MathViewsTest(TestCase):

    def setUp(self):
        Author.objects.create(nick='t_testowy', email='test.testowy@hogwarts.com', bio='test bio')
        self.a1 = Author.objects.get(nick='t_testowy')
        Post.objects.create(title='title test', content='content test', author_id=self.a1)

    def test_posts_main_page(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<b>To część stała szablonu głównego.</b>', response.content.decode())

    def test_posts_details(self):
        response = self.client.get('/posts/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<td>content test</td>', response.content.decode())

    def test_authors_main_page(self):
        response = self.client.get('/posts/authors')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<li><a href="/posts/authors/1">content test</a></li>', response.content.decode())

    def test_authors_details(self):
        response = self.client.get('/posts/authors/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<td>test.testowy@hogwarts.com</td>', response.content.decode())