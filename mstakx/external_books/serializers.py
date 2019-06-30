from rest_framework import serializers

"""
Purpose: class which transforms the external api response into rrequired format, by removing 
         unwanted fields
Author : Ashkar Ali 

"""
class ExternalBookSerializer(serializers.Serializer):
    name = serializers.CharField()
    isbn = serializers.CharField()
    authors = serializers.ListField(child=serializers.CharField())
    country = serializers.CharField()
    numberOfPages = serializers.IntegerField()
    publisher = serializers.CharField()
    released = serializers.DateField() 