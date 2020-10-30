from rest_framework import serializers
from books.models import Book
from users.models import Profile

class BookSerializer(serializers.ModelSerializer): 
  class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'details')

class ProfileSerializer(serializers.ModelSerializer): 
  class Meta:
        model = Profile
        fields = ('bio', 'birth_date', 'contact', 'projects')