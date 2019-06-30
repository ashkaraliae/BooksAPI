from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books.views import BookList, BookDetail, SearchBook

class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func.view_class,BookList)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=[2])
        self.assertEquals(resolve(url).func.view_class,BookDetail)
    
    def test_detail_url_resolves(self):
        url = reverse('search', args=['A Game of Thrones'])
        self.assertEquals(resolve(url).func.view_class,SearchBook)
