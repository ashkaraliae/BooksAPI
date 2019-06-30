from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/external-books/', include('external_books.urls')),
    path('api/v1/', include('books.urls')),
]
