from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from api.models import Book, LibUser, RentBook
from .serializers import BookSerializer, LibUserSerializer, RentBookSerializer
from .pagination import CustomPagination


class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibuserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer
    pagination_class = CustomPagination


class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer


