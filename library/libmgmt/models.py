from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

User = settings.AUTH_USER_MODEL
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="authored")
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=timezone.now()+timedelta(days=14))

    def clean(self):
        if Checkout.objects.filter(book=self.book, return_date__gt=timezone.now()).exists():
            raise ValidationError("This book is already checked out")
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    @classmethod
    def remove_overdue_records(cls):
        cls.objects.filter(return_date__lt=timezone.now()).delete()