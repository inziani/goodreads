from django.shortcuts import render
from django import forms
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count


from .models import Book, Review

class BookListView(ListView): 
  model = Book
  context_object_name = 'book_list'
  template_name = 'book_list.html'

class BookDetailView(DetailView): 
  model = Book
  template_name = 'book_detail.html'

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ('author', 'review', 'design', 'usability', 'content')

@login_required
def add_review(request, pk):
  book = get_object_or_404(Book, pk=pk)
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      review = form.save(commit = False)
      review.book = book
      review.save()
      return redirect ('book_detail', pk=book.pk)
  else:
    form = ReviewForm()
  return render(request, 'review.html', {'form': form})


class BookNewEntryView(CreateView):
  model = Book
  template_name = 'new_entry.html' 
  fields = ['title', 'author', 'cover', 'description', 'details']

def  avg_vote (request, pk):
  book = get_object_or_404(Book, pk=pk)
  if request.method == 'GET':
    tally = design = book.review.design.count()
  return tally
  





