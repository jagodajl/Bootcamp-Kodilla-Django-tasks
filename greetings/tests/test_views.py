from django.test import TestCase, Client


class MathViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_greetings(self):
        response = self.client.get('/greetings/')
        self.assertIn('Hello World!', response.content.decode())

    def test_greetings(self):
        response = self.client.get('/greetings/test')
        self.assertIn('Hello Test!', response.content.decode())