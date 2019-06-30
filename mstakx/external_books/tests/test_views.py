from django.test import TestCase,Client
from django.urls import reverse
import requests
from external_books.constants import BASE_URL

class TestExternalBooks(TestCase):

    """
    Purpose: Test cases for external_books.views
    Author: Ashkar Ali

    """

    def setUp(self):
        self.client = Client()
        self.external_book_url = reverse('external_book')


    def test_external_book_view_GET(self):
        response = requests.get(BASE_URL)
        self.assertTrue(response.ok)

    def test_external_book_when_url_wrong(self):
        response = requests.get("https://www.anapioficeandfire.com/api/booksssss/")
        self.assertEquals(response.status_code,404)


