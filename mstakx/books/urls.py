from django.contrib import admin
from django.urls import path, include
from . import views

"""
    Purpose: URL mappings for books app
    Author: Ashkar Ali
"""

urlpatterns = [
    path('/books', views.BookList.as_view(), name="list" ),
    path('/books/<int:pk>', views.BookDetail.as_view(), name = "detail"),
    path('/books/search/<search_string>', views.SearchBook.as_view(), name="search" ),

]