from django.test import SimpleTestCase
from django.urls import reverse, resolve
from external_books.views import ExternalBookView

class TestUrls(SimpleTestCase):

    def test_external_book_view_url_resolves(self):
        url = reverse('external_book')
        self.assertEquals(resolve(url).func.view_class,ExternalBookView)