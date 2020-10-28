from django.contrib.auth.models import AbstractUser 
from django.utils import timezone
from django.contrib.auth import get_user_model 
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import roles

# Create your models here.

class CustomUser(AbstractUser):
  user = models.CharField(max_length=10, default='user')
  email = models.EmailField(unique = True)
  is_active = models.BooleanField(default=True)
  is_member = models.BooleanField(default=True)
  date_joined = models.DateTimeField(default=timezone.now)
  user_type = models.PositiveSmallIntegerField(choices=roles.USER_TYPE_CHOICES, default=2)

  def __str__(self):
    return 'Email: {}'.format(self.email)


class Profile(models.Model):
  user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE, related_name="profile")
  bio = models.CharField(max_length=255,blank=True,null=True)
  birth_date = models.DateField(null=True, blank = True)
  profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
  contact = models.CharField(max_length=144, blank=True, null=True)
  projects = models.URLField(max_length=200, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return 'User: {}'.format(self.user)



