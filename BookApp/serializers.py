from rest_framework import serializers
from BookApp.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','authorname', 'expertise', 'authoremail']


class BookSerializer(serializers.ModelSerializer):
    bookauthor = AuthorSerializer()
    
    class Meta:
        model = Book
        fields = ['bookname','bookauthor','isbn_number','price']


class BookSaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['bookname','bookauthor','isbn_number','price']