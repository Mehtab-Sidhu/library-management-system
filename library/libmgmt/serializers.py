from rest_framework import serializers
from .models import Book, Author, Checkout

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'is_active', 'created']

class AuthorSerializer(serializers.ModelSerializer):
    authored_books = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ['id', 'name', 'authored_books']
    
    def get_authored_books(self, author):
        books = Book.objects.filter(author=author)
        book_serializer = BookSerializer(books, many=True)
        return book_serializer.data
    
class CheckoutSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book.title', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Checkout
        fields = ['id', 'book', 'book_name', 'user', 'username', 'checkout_date', 'return_date']
