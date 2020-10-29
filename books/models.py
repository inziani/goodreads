from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models



class Book(models.Model):

  class Rating(models.IntegerChoices):
    Zero = 0
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
  title = models.CharField(max_length = 200)
  author = models.CharField(max_length = 200)
  cover = models.ImageField(upload_to = 'covers/')
  description = models.TextField()
  details = models.URLField(max_length=200, blank=True)
  likes = models.ManyToManyField(get_user_model(), related_name = 'book_likes', blank = True)
  design = models.IntegerField(choices=Rating.choices, default=0)
  usability = models.IntegerField(choices=Rating.choices, default=0)
  content = models.IntegerField(choices=Rating.choices, default=0)


  def __str__(self): 
    return self.title

  def get_absolute_url(self):
    return reverse('book_detail', args=[str(self.id)])

class Review(models.Model):  
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
  review = models.TextField()
  author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, )

  def __str__(self): 
    return self.review


  def get_absolute_url(self):
    return reverse('review', args=[str(self.id)])
