from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Enable search functionality
    search_fields = ('title', 'author')

    # Add a filter for publication year
    list_filter = ('publication_year',)