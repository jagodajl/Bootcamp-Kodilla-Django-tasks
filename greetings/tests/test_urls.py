from unittest import TestCase
from django.urls import resolve
from greetings.views import world, imie


class TestUrls(TestCase):
    def test_resolution_greetings(self):
        resolver = resolve('/greetings/')
        self.assertEqual(resolver.func, world)

    def test_resolution_name(self):
        resolver = resolve('/greetings/test')
        self.assertEqual(resolver.func, imie)
