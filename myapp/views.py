# myapp/views.py

from django.shortcuts import render
from .models import Author, Book, Publisher
from .forms import AuthorForm, BookForm, PublisherForm, SearchForm


def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'myapp/add_author.html', context)


def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'myapp/add_book.html', context)


def add_publisher(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'myapp/add_publisher.html', context)


def search(request):
    form = SearchForm(request.POST or None)
    results = []
    if form.is_valid():
        search_text = form.cleaned_data['search_text']
        results = Book.objects.filter(title__icontains=search_text)
    context = {'form': form, 'results': results}
    return render(request, 'myapp/search.html', context)

def inicio (request):
    return render(request, 'myapp/inicio.html')
