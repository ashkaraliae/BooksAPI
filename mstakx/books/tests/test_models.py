from django.test import TestCase
from books.models import Book

class TestModels(TestCase):

    def setUp(self):
        self.book1 = Book.objects.create(
            name = "A Feast for Crows",
            isbn = "978-0553801507",
            authors = ["George R. R. Martin"],
            country = "United Status",
            number_of_pages = 784,
            publisher = "Bantam Books",
            release_date = "2005-11-08"
        )

    def book_is_created(self):
        self.assertEquals(self.book1.id, 1)
        self.assertEquals(response.status_code, 200)
