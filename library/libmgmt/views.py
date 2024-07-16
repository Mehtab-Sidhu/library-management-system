from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.serializers import BaseSerializer
from .models import Author, Book, Checkout
from .serializers import BookSerializer, AuthorSerializer, CheckoutSerializer
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    # filterset_fields = ['is_active']
    filterset_fields = {
        'is_active': ['exact'],
        'created': ['exact', 'range'],
    }

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer  

