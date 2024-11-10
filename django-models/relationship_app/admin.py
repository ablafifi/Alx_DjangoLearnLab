from django.contrib import admin
from .models import Book  # Ensure that the Book model is imported

# Define the BookAdmin class
class BookAdmin(admin.ModelAdmin):
    # Specify any display options or customizations
    list_display = ('title', 'author')  # Replace with actual field names from your Book model

# Register the Book model with the BookAdmin
admin.site.register(Book, BookAdmin)