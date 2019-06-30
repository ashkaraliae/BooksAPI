from django.contrib import admin
from django.urls import path, include
from . import views

"""
    Purpose: url mapping for external_books app
    Author: Ashkar Ali
    
"""

urlpatterns = [
    path('', views.ExternalBookView.as_view(), name = "external_book"),
]
