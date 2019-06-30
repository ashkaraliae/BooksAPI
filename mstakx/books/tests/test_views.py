from django.test import TestCase,Client
from django.urls import reverse
from books.models import Book
from books.views import SearchBook
import json

class TestViews(TestCase):

    """
    Purpose: Test cases for books.views
    Author: Ashkar Ali

    """

    def setUp(self):
        self.client  = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=[2])
        self.search_url = reverse('search', args=['A Game of Thrones'])
        self.search_url_date = reverse('search', args=['1996-08-01'])
        self.arg1 = '1996-08-01'
        self.book1 = Book.objects.create(
            name = "A Feast for Crows",
            isbn = "978-0553801507",
            authors = ["George R. R. Martin"],
            country = "United Status",
            number_of_pages = 784,
            publisher = "Bantam Books",
            release_date = "2005-11-08"
        )

    def test_book_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_book_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)

    def test_book_list_POST_adds_new_book(self):
        response = self.client.post(self.list_url,{
            "name": "A Feast for Crows",
            "isbn": "978-0553801507",
            "authors": ["George R. R. Martin"],
            "country": "United Status",
            "number_of_Pages": 784,
            "publisher": "Bantam Books",
            "release_date": "2005-11-08T00:00:00"
        })
        self.assertEquals(response.status_code, 200)

    def test_book_list_POST_no_data(self):
        response = self.client.post(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_book_detail_DELETE(self):
        book2 = Book.objects.create(
            name = "A Feast for Crows",
            isbn = "978-0553801507",
            authors = ["George R. R. Martin"],
            country = "United Status",
            number_of_pages = 784,
            publisher = "Bantam Books",
            release_date = "2005-11-08"
        )
        response = self.client.delete(self.detail_url, json.dumps({
            'id': 1
        }))
        self.assertEquals(response.status_code, 204)

    def test_search_book_when_data_is_found(self):
        response = self.client.get(self.search_url)
        self.assertEquals(response.status_code, 200)

    def test_search_book_when_string_is_date(self):
        response = self.client.get(self.search_url_date)
        self.assertEquals(response.status_code, 200)

    def test_is_date_when_input_is_date(self):
        self.assertEquals(SearchBook.is_date( self.arg1),True)

    def test_is_date_when_input_is_not_date(self):
        self.arg2 = 'not-a-date' 
        self.assertEquals(SearchBook.is_date( self.arg2),False)


