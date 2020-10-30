from django.shortcuts import render

from rest_framework import generics
from books.models import Book
from users.models import Profile
from .serializers import BookSerializer, ProfileSerializer

# Create your views here.

class BookAPIView(generics.ListAPIView): 
  queryset = Book.objects.all() 
  serializer_class = BookSerializer

class ProfileAPIView(generics.ListAPIView): 
  queryset = Profile.objects.all() 
  serializer_class = ProfileSerializer
