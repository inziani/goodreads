from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models


class Book(models.Model):
  title = models.CharField(max_length = 200)
  author = models.CharField(max_length = 200)
  cover = models.ImageField(upload_to = 'covers/')
  description = models.TextField()
  details = models.URLField(max_length=200, blank=True)
  likes = models.ManyToManyField(get_user_model(), related_name = 'book_likes')

  def __str__(self): 
    return self.title

  def get_absolute_url(self):
    return reverse('book_list', args=[str(self.id)])

