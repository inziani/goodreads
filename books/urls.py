
from django.urls import path
from . import views
from .views import BookListView, BookDetailView, add_review, BookNewEntryView

urlpatterns = [
  

path('', BookListView.as_view(), name='book_list'),
path('<int:pk>/', BookDetailView.as_view(), name='book_detail'), 
path('book/<int:pk>/review/', views.add_review, name = 'review'),
path('book/new/', BookNewEntryView.as_view(), name='new_entry'),
# path('book/<int:pk>/vote/', VoteView.as_view(), name='vote'),
# path('book/<int:pk>/vote/', views.vote, name='vote'),

]