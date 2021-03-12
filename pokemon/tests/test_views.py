from django.test import TestCase
from django.urls import resolve, reverse
from pokemon.views import HomePageView


class HomePageTests(TestCase):
    """
    Test Suite for all tests related to home page
    """

    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def test_home_page_renders_correct_html_template(self):
        self.assertTemplateUsed(self.response, 'pokemon/home.html')

    def test_home_page_resolve_correct_view(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    def test_home_page_contains_correct_text(self):
        self.assertContains(self.response, 'Pokemon')
