from django.contrib import admin
from .models import Book, Author, Checkout
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'created', 'title', 'author']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Checkout)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'checkout_date', 'return_date']