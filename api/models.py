from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)


class LibUser(models.Model):
    name = models.CharField(max_length=100)


class RentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(LibUser, on_delete=models.CASCADE)
    rentDate = models.DateField(auto_now_add=True)
    returneddate = models.DateField(null=True, blank=True)
