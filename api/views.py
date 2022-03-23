from django.shortcuts import render
from rest_framework import viewsets
from api.models import Book, LibUser, RentBook
from .serializers import BookSerializer, LibUserSerializer, RentBookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book
    serializer_class = BookSerializer


class LibuserViewSet(viewsets.ModelViewSet):
    queryset = LibUser
    serializer_class = LibUserSerializer


class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook
    serializer_class = RentBookSerializer


