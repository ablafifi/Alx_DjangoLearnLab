from django.contrib import admin
from .models import Book  # Ensure that the Book model is imported

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Define the BookAdmin class
class BookAdmin(admin.ModelAdmin):
    # Specify any display options or customizations
    list_display = ('title', 'author')  # Replace with actual field names from your Book model

# Register the Book model with the BookAdmin
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)