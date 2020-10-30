from django.urls import path

from .views import BookAPIView, ProfileAPIView

urlpatterns = [

path('', BookAPIView.as_view()),
path('profile/', ProfileAPIView.as_view()),

]