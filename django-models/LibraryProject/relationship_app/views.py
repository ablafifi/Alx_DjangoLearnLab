from django.shortcuts import render

from .models import Book  # Adjust the model import if your Book model is in another app

from django.views.generic.detail import DetailView
from .models import Library  # Adjust the import if your Library model is in another app

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
