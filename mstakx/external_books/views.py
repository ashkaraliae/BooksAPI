from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import status
import requests
from .serializers import ExternalBookSerializer
from .constants import BASE_URL

class ExternalBookView(APIView):

    """
    Purpose: API which queries Ice And Fire API and returns data based on the
             name of the book
    Author: Ashkar Ali

    """

    def get(self,request):
        try:
            name = request.GET["name"]
            response = requests.get(BASE_URL)
            json_data = json.loads(response.text)
            for book in json_data:
                if(book['name'] == name):
                    serializer = ExternalBookSerializer(book)
                    return Response({"status_code":200,"status": "success","data": serializer.data})
                else:
                    continue
            return Response({"status_code":200,"status": "success","data": []})
        except Exception as e:
            return Response({"status_code": 400, "status": "fail", "error": str(e) })
        
