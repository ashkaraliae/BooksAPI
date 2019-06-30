from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    isbn = serializers.CharField()
    authors = serializers.ListField(child=serializers.CharField())
    country = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    publisher = serializers.CharField()
    release_date = serializers.DateField()   

    def create(self, validated_data):
        """
        Create and return a new `Book` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Book` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.authors = validated_data.get('authors', instance.authors)
        instance.country = validated_data.get('country', instance.country)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance