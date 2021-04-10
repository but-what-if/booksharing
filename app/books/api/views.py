from rest_framework import viewsets, filters
from books.models import Book, Author, Category
from books.api.serializers import BookSerializer, AuthorSerializer, CategorySerializer
from books.api.filters import BookFilter, AuthorFilter, CategoryFilter
from django_filters.rest_framework import DjangoFilterBackend


# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookInstanceView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['condition']
    # filterset_fields = ['condition']
    filterset_class = BookFilter


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['last_name']
    filterset_class = AuthorFilter


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name']
    filterset_class = CategoryFilter
