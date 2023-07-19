from django.db import models

# Create your models here.
class Author(models.Model):
    authorname = models.CharField(max_length=200)
    expertise = models.CharField(max_length=200)
    authoremail = models.EmailField()


class Book(models.Model):
    bookname = models.CharField(max_length=200)
    bookauthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn_number = models.CharField(max_length=100)
    price = models.FloatField()