from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from django.db.models import Q
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404
from dateutil.parser import parse
import pdb;

class BookList(APIView):
    """
    Purpose:  List all Books or create a new Book.
    Author:   Ashkar Ali

    """
    def get(self, request):
        try:
            book_obj = Book.objects.all()
            serializer = BookSerializer(book_obj, many=True)
            return Response({"status_code": 200, "status": "success", "data": serializer.data})
        except Exception as e:
            return Response({"status_code": 400, "status": "fail", "error": str(e) })
    
    def post(self, request):
        try:
            serializer = BookSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status_code": 201, "status": "success", "data": {"book": serializer.data}}, status=201)
            return Response({"status_code": 400, "status": "fail", "error": serializer.errors})
        except Exception as e:
            return Response({"status_code": 400, "status": "fail", "error": str(e) })


class BookDetail(APIView):
    """
    Purpose: Retrieve, update or delete a Book when id is given
    Author: Ashkar Ali

    """
    def get(self,request,pk):
        try:
            book_obj = get_object_or_404(Book.objects.all(), pk=pk)
            serializer = BookSerializer(book_obj)
            return Response({"status_code": 200, "status": "success", "data": serializer.data})
        except Exception as e:
            return Response({"status_code": 400, "status": "fail", "error": str(e) })

    def patch(self, request, pk):
        try:
            saved_book = get_object_or_404(Book.objects.all(), pk=pk)
            book_name = saved_book.name
            serializer = BookSerializer(instance=saved_book ,data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status_code": 200, "status": "success", "message": "The book "+book_name+" was updated successfully", "data":serializer.data })
            return Response({"status_code": 400, "status": "fail", "error": serializer.errors})
        except Exception as e:
            return Response({"status_code": 400, "status": "fail", "error": str(e) })
    
    def delete(self, request, pk):
        try:
            saved_book = get_object_or_404(Book.objects.all(), pk=pk)
            book_name = saved_book.name
            saved_book.delete()
            return Response({"status_code": 204, "status": "success","message": "The book "+book_name+" was deleted successfully", "data":[] }, status=204)
        except Exception as e:
            return Response({"status_code": 400, "status": "fail", "error": str(e) })

class SearchBook(APIView):

    """
    Purpose : To search and return data  when name (string), country (string),
              publisher (string) or release date (year, integer) is given
    Author : Ashkar Ali

    """
    
    def get(self, request,search_string):
        try:
            if (SearchBook.is_date(search_string)):
                book_obj = Book.objects.filter(release_date=search_string)
            else:
                book_obj = Book.objects.filter(Q(name=search_string)|Q(country=search_string)\
                        |Q(publisher=search_string))
            serializer = BookSerializer(book_obj, many=True)
            return Response({"status_code": 200, "status": "success","data": serializer.data })
        except Exception as e:
            return Response({"status_code": 400, "status": "fail", "error": str(e) })

    def is_date(search_string,fuzzy=False):
        """
        Returns whether the string can be interpreted as a date.
        :param string: str, string to check for date
        :param fuzzy: bool, ignores unknown tokens in string if True
        """
        try: 
            parse(search_string,fuzzy=fuzzy)
            return True

        except ValueError:
            return False



    