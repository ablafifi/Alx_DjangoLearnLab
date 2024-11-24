# Import Django models
from .models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# Query 2: List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Access related books via the ManyToManyField
    return books

# Query 3: Retrieve the librarian for a given library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # Access the related librarian via the OneToOneField
    return librarian
